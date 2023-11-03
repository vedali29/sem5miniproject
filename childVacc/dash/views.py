# dashboardviews.py
from django.shortcuts import render
from login.models import UserProfile
from appointment.models import Appointment
from login.form import LoginForm

def profile_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        appointments = Appointment.objects.filter(user=request.user)

        context = {
            'user_profile': user_profile,
            'appointments': appointments,
        }

        return render(request, 'profile.html', context)
    except:
        form = LoginForm()
        user_profile = UserProfile.objects.get(id=1)
        appointments = Appointment.objects.filter(id=5)
        context = {
            'user_profile': user_profile,
            'appointments': appointments,
        }
        return render(request,'login.html',{'form':form,'error':'Not loggedin'})
