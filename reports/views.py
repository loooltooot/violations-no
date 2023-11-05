from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from . import forms

# Create your views here.

class RegisterView(generic.CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'reports/register.html'
    
    def get_success_url(self):
        return reverse_lazy('reports:login')

def logout_user(request):
    logout(request)
    return redirect('reports:register')

class LoginUserView(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'reports/login.html'

    def get_success_url(self):
        return reverse_lazy('reports:register')