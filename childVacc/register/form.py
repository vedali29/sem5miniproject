# forms.py

from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['child_name', 'parent_name', 'relationship_to_child', 'child_birthdate', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
