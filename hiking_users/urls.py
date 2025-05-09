from django.urls import path
from . import views

# URL patterns for user registration
urlpatterns = [
    path('register/', views.register, name='register'),
]
