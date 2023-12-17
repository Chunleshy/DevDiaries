from django.apps import AppConfig

# This configuration class defines the configuration for the 'blog' app.

class BlogConfig(AppConfig):
    # Specifies the configuration for the 'blog' app.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
