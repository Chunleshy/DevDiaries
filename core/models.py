# Import necessary modules from Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Define a custom user model, inheriting from AbstractUser
class CustomUser(AbstractUser):
    # Add an email field with uniqueness constraint
    email = models.EmailField(unique=True)
    
    # Specify that the email field should be used as the username field
    USERNAME_FIELD = 'email'

    # Specify additional fields that will be required in the forms
    REQUIRED_FIELDS = ('username',)

    # Define a human-readable string representation for the user object
    def __str__(self):
        return self.email



# <form action="" method="POST">
#                         <p><strong>{{follow_count}} follower{{ follow_count|pluralize}}</strong></p>
#                         {% csrf_token %}
#                         {% if request.user.is_authenticated %}
#                             {% if follow %}
#                                 {% if following %}
#                                     <button class="btn btn-outline-primary btn-lg">Following</button>
#                                 {% else %}
#                                     <button class="btn btn-primary btn-lg">Follow</button>
#                                 {% endif %}
#                             {% endif %}
#                         {% else %}
#                             <p>Login to follow this profile</p>
#                         {% endif %}
#                     </form>