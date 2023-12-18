from django.urls import path
from . import views

# Defines a URL pattern for the login functionality.

urlpatterns = [
    # Maps the 'login/' URL to the 'sign_in' view.
    path('login/', views.sign_in, name='login')
]
