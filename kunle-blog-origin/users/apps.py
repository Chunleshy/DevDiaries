from django.apps import AppConfig

# Configures the 'users' app within the Django project.

class UsersConfig(AppConfig):
    # Specifies the configuration for the 'users' app.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
