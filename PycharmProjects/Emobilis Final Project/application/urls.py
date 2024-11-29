from django.contrib import admin
from django.urls import path, include

from application import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),  # Home page
    path('accounts/', include('django.contrib.auth.urls')),  # Includes Django's auth URLs
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
]
