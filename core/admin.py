from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
# Define a custom admin class for CustomUser model, inheriting from UserAdmin
class CustomUserAdmin(UserAdmin):
    # Define fieldsets for adding a new user in the admin interface
    add_fieldsets = (
        (
            None,
            {
                # Additional CSS classes for styling
                "classes": ("wide",),
                # Fields displayed for adding a new user
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )

# Register the CustomUser model with the CustomUserAdmin class in the Django admin interface
admin.site.register(CustomUser, CustomUserAdmin)
