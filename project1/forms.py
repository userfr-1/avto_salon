from django import forms
from .models import *

class AvtoSalonForms(forms.ModelForm):
    class Meta:
        model = Autosalon
        fields = ['title', 'context', 'email', 'phone', 'address']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Salon nomini kiriting'
            }),
            'context': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Salon haqida ma\'lumot'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email manzili'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telefon raqami'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Manzil'
            }),
        }
