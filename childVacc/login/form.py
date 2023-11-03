# # forms.py

# from django import forms
# from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile

# class LoginForm(AuthenticationForm):
#     class Meta:
#         model = UserProfile
#         fields = ['email', 'password']
#         widgets = {
#             'password': forms.PasswordInput(),
#         }



# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserProfile

class LoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

    class Meta:
        model = UserProfile
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


