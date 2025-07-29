from django import forms
from .models import *

class AvtoSalonForms(forms.ModelForm):
    class Meta:
        model = Autosalon
        fields = ['title','context','email','phone','address']