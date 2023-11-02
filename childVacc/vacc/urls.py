from django.contrib import admin
from django.urls import path
from . import views

# List of views
view_list = ["about", "appointment", "blog", "contact", "doctors", "forPass", "gallery", "login", "privacy", "profile", "registration", "terms"]

urlpatterns = [
    path('', views.child, name='child'),  # Assuming 'child' is a valid view function
    
    # Dynamically create paths for each view in the list
    *[path(f'{i}/', getattr(views, i), name=i) for i in view_list],
    
    path('main',views.register_user,name="reg_user"),
]