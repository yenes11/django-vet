from dataclasses import fields
from pyexpat import model
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse

from .models import Owner
from .forms import RegistrationForm


class RegistrationView(CreateView):
    model = Owner
    fields = ['email', 'password', 'name', 'surname', 'phone']
    template_name = 'users/register.html'
    forms_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += f'?next={next_url}'
        
        return success_url

class ProfileView(UpdateView):
    model = Owner
    fields = ['name', 'surname', 'phone']
    template_name = 'users/profile.html'

    def get_success_url(self) -> str:
        return reverse('index')

    def get_object(self):
        return self.request.user


