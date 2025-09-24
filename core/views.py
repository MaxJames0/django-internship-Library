from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
