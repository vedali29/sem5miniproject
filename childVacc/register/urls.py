# urls.py

from django.urls import path
from .views import registration_view

urlpatterns = [
    # Other URL patterns
    path('registration/', registration_view, name='registration'),
]
