# appointmentviews.py
from django.shortcuts import render, redirect
from .forms import AppointmentForm
from django.template import loader
from django.http import HttpResponse

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # You can add a success message or redirect to a thank you page
            # return redirect('profile')  # Replace 'profile' with the appropriate URL
            template = loader.get_template('profile.html')
         # firebase_data = get_firebase_data()
            return HttpResponse(template.render())
    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {'form': form})
