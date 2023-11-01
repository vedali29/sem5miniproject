# from django.http import HttpResponse
from django.template import loader
import json
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

def child(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def blog(request):
  template = loader.get_template('blog.html')
  return HttpResponse(template.render())

# def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def appointment(request):
  template = loader.get_template('appointment.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())

def doctors(request):
  template = loader.get_template('doctors.html')
  return HttpResponse(template.render())

def forPass(request):
  template = loader.get_template('forgetpass.html')
  return HttpResponse(template.render())

def gallery(request):
  template = loader.get_template('gallery.html')
  return HttpResponse(template.render())

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def privacy(request):
  template = loader.get_template('privacy.html')
  return HttpResponse(template.render())

def profile(request):
  template = loader.get_template('profile.html')
  return HttpResponse(template.render())

def registration(request):
  template = loader.get_template('registration.html')
  return HttpResponse(template.render())

def terms(request):
  template = loader.get_template('terms.html')
  return HttpResponse(template.render())


def login(request):
    if request.method == 'POST':
        # Get the email and password from the login form
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Your Firebase project's API key
        api_key = 'YOUR_FIREBASE_API_KEY'

        # Firebase Authentication REST API endpoint for email/password sign-in
        endpoint = f'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}'

        # Create a data payload for the request
        data = {
            'email': email,
            'password': password,
            'returnSecureToken': True,
        }

        # Make a POST request to Firebase Authentication REST API
        response = requests.post(endpoint, data=json.dumps(data), headers={'Content-Type': 'application/json'})

        # Parse the JSON response
        result = response.json()

        # Check if the login was successful
        if 'idToken' in result:
            # Authentication successful, you can store the user's token in the session or perform other actions
            # For example, storing the token in the session:
            request.session['firebase_token'] = result['idToken']
            
            # Redirect to a success page
            return redirect('success_page')

        else:
            # Authentication failed, display an error message
            messages.error(request, 'Invalid email or password.')

    # Render the login page template
    return render(request, 'login.html')