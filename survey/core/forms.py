# forms.py
from django import forms
from .models import Survey

class MyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'
