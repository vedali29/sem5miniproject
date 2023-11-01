from django import forms
from .models import UserProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['child_name', 'parent_name', 'email', 'password']  # Add other fields as needed
        widgets = {
            'password': forms.PasswordInput(),
        }