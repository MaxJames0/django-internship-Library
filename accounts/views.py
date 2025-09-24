from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from .models import User
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView

from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model, logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

user = get_user_model()

class RegisterView(CreateView):
    model = user
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')

class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('accounts:profile')
    
    def get_initial(self):
        initial = super().get_initial()
        phone = self.request.GET.get('phone')
        if phone:
            initial['username'] = phone
        return initial
    
    
class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = "accounts/profile.html"  
    
    
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('accounts:login')


