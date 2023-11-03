# loginviews.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from login.models import UserProfile
from appointment.models import Appointment
from .form import LoginForm

def login_view(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if request.POST['username']!=None:
            emaill = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=emaill, password=password)
            if emaill!=None:
                try:
                    # Redirect to a success page or dashboard
                    user_profile = UserProfile.objects.get(email=emaill)
                    appointments = Appointment.objects.filter(email=emaill)

                    context = {
                        'user_profile': user_profile,
                        'appointments': appointments,
                    }
                    return render(request, 'profile.html',context)  # Create a success template
                except:
                    return render(request, 'login.html', {'form': form, 'error': 'user mismatch'})
            else:
                # Handle invalid login credentials
                return render(request, 'login.html', {'form': form, 'error': 'Invalid login credentials'})
        else:
            return render(request,'login.html',{'form':form,'error':f'{request.POST}'})
    else:
        form = LoginForm()
        # print(request.POST)
        return render(request, 'login.html', {'form': form})
