from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class LoginView(FormView):
    template_name = 'accounts/login.html' 
    form_class = AuthenticationForm
    success_url = reverse_lazy('app_name:dashboard')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

class SignupView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('app_name:login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        return response