from django.shortcuts import render
from django.views.generic import TemplateView , FormView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.

class HomeView(TemplateView):
    template_name = 'core/home.html'
    
    
class ContactView(FormView):
    template_name = "core/contact_us.html"
    form_class = ContactForm
    success_url = reverse_lazy("core:contact")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message was sent successfully!")
        return super().form_valid(form)
