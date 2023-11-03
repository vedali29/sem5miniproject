# forms.py

from django import forms
from .models import UserProfile

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
