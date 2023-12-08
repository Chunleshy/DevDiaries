from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile, Blog

# Signal receiver function triggered after a user is saved
@receiver(post_save, sender=get_user_model()) 
def create_profile(sender, instance, created, **kwargs):
    # If a new user is created, a Profile instance is also created
    if created: 
         Profile.objects.create(user=instance, username=instance.username, email=instance.email)
  
# Signal receiver function triggered after a Profile is saved
@receiver(post_save, sender=Profile) 
def update_profile(sender, instance, created, **kwargs):
    # If a new Profile is created, do nothing
    if created:
        pass 
    else:
        # If an existing Profile is updated, update the associated User fields
        user = instance.user # current profile that you want to update with logged in user
        user.email = instance.email  # instance of profile model here
        user.username = instance.username
        user.first_name = instance.first_name
        user.last_name = instance.last_name
        user.save()


        
