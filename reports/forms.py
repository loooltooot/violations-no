from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.utils.translation import gettext as _

from .models import MyUser

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('last_name', 'first_name', 'patronymic', 'email', 'tel', 'username', 'password1', 'password2')
        widgets = {
            'last_name': forms.TextInput(attrs={'required': ''}),
            'first_name': forms.TextInput(attrs={'required': ''}),
            'email': forms.EmailInput(attrs={'required': ''}),
        }

class LoginUserForm(AuthenticationForm):
    class Meta:
        model = MyUser