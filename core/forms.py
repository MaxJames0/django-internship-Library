from django import forms
from .models import Contact_us

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_us
        fields = ['your_name', 'your_email', 'your_message']