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


class ProfileUpdateView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "accounts/update_profile.html"
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user
    
    
class UserListView(ListView):
    model = User
    template_name = "accounts/users_list.html"
    context_object_name = 'users'

class UserUpdateView(UpdateView):
    model = user
    form_class = ProfileForm
    template_name = "accounts/users_update.html"
    success_url = reverse_lazy('accounts:users_list')


class UserDeleteView(DeleteView):
    model = user
    template_name = "accounts/users_delete.html"
    success_url = reverse_lazy('accounts:users_list')


    
    
class UserCustomCreateView(CreateView):
    model = User
    form_class = CustomUser
    template_name = 'accounts/custom_user_create.html'
    success_url = reverse_lazy('accounts:users_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        # set password properly
        user.set_password(form.cleaned_data["password1"])
        user.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)  # debug in terminal
        return super().form_invalid(form)
    

