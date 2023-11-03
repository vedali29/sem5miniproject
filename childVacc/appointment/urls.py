# urls.py
from django.urls import path
from .views import appointment

urlpatterns = [
    # Other URL patterns...
    path('appointment/', appointment, name='appointment'),
]
