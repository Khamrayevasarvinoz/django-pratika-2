from django.forms import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea,EmailInput


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['tel_nomer', 'email', 'level', 'message']
        widgets = {
            'tel_nomer':TextInput(attrs={
             'placeholder':'your phone',   
            }),
              'email':EmailInput(attrs={
             'placeholder':'your email',   
            }),
              'level':TextInput(attrs={
             'placeholder':'your level',   
            }),
              'message':TextInput(attrs={
             'placeholder':'your message',
             "class":'beki'   
            })    
        }