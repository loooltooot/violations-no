from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext as _
import re

from .models import MyUser, Report

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('last_name', 'first_name', 'patronymic', 'email', 'tel', 'username', 'password1', 'password2')
        widgets = {
            'last_name': forms.TextInput(attrs={'required': ''}),
            'first_name': forms.TextInput(attrs={'required': ''}),
            'email': forms.EmailInput(attrs={'required': '', 'placeholder': ' '}),
            'tel': forms.TextInput(attrs={'id': 'phone-mask'}),
        }

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = MyUser

class CreateReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('car_plate', 'report_description')
        widgets = {
            'car_plate': forms.TextInput(attrs={'class': 'car_plate', 'placeholder': 'X111XX11'}),
        }

    def clean_car_plate(self):
        car_plate = self.cleaned_data['car_plate'].upper()

        regex = r"^(([АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{1,2})(\d{2,3})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ]{2})(\d{2})|(\d{3}(?<!000)(C?D|[ТНМВКЕ])\d{3}(?<!000))(\d{2}(?<!00))|([ТСК][АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]\d{4}(?<!0000))(\d{2})|(\d{3}(?<!000)[АВЕКМНОРСТУХ])(\d{2})|(\d{4}(?<!0000)[АВЕКМНОРСТУХ])(\d{2})|([АВЕКМНОРСТУХ]{2}\d{4}(?<!0000))(\d{2})|([АВЕКМНОРСТУХ]{2}\d{3}(?<!000))(\d{2,3})|(^Т[АВЕКМНОРСТУХ]{2}\d{3}(?<!000)\d{2,3}))"
        pattern = re.compile(regex)

        if not pattern.match(car_plate):
            raise forms.ValidationError(_('Enter valid licence plate number'))
        
        return car_plate