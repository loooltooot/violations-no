from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from . import forms, models

# Create your views here.

class RegisterView(generic.CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'reports/register.html'

    def form_valid(self, form):
        form.save()
        new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        login(self.request, new_user)
        return redirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse_lazy('reports:index')

def logout_user(request):
    logout(request)
    return redirect('reports:login')

class LoginUserView(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'reports/login.html'

    def get_success_url(self):
        return reverse_lazy('reports:index')

class IndexView(LoginRequiredMixin, generic.ListView):
    model = models.Report
    template_name = 'reports/index.html'
    redirect_field_name = ''

    def get_queryset(self):
        return models.Report.objects.filter(user=self.request.user)

class CreateReportView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.CreateReportForm
    template_name = 'reports/create_report.html'
    redirect_field_name = ''

    def get_success_url(self):
        return reverse_lazy('reports:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateReportView, self).form_valid(form)
    
class DeleteReportView(LoginRequiredMixin, generic.DeleteView):
    model = models.Report
    redirect_field_name = ''

    def get_success_url(self):
        return reverse_lazy('reports:index')