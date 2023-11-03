# registerviews.py

from django.shortcuts import render, redirect
from .form import RegistrationForm
from login.form import LoginForm
from login.models import UserProfile

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        login_form = LoginForm(request.POST)
        if form.is_valid() and login_form.is_valid():
            registration = form.save()  # Save the Registration instance
            UserProfile.objects.create(
                registration=registration,
                email=login_form.cleaned_data['email'],
                password=login_form.cleaned_data['password']
            )
            # You may want to add logic to handle user authentication or send a confirmation email here
            return render(request, 'login.html', {'form': login_form})  # Create a success template
    else:
        form = RegistrationForm()
        login_form = LoginForm()

    return render(request, 'registration.html', {'form': form, 'login_form': login_form})

