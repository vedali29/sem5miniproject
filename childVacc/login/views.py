# loginviews.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .form import LoginForm
from register.form import RegistrationForm
from dash.forms import UserProfile

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page or dashboard
                return render(request, 'profile.html')  # Create a success template
            else:
                # Handle invalid login credentials
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = LoginForm()
        # print(request.POST)

    return render(request, 'login.html', {'form': form})
