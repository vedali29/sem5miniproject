# dashboardviews.py
from django.shortcuts import render
from login.models import UserProfile
from appointment.models import Appointment

def profile_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    appointments = Appointment.objects.filter(user=request.user)

    context = {
        'user_profile': user_profile,
        'appointments': appointments,
    }

    return render(request, 'profile.html', context)
