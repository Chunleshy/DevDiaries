# Importing necessary modules or classes
from django.apps import AppConfig

# Creating a class BlogappConfig that inherits from AppConfig
class BlogappConfig(AppConfig):
    # Define the default auto field for models as BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Set the name of the app as 'blogapp'
    name = 'blogapp'
    
    # Define a method 'ready' that is executed when the application is ready
    def ready(self):
        # Import signals from the blogapp module
        import blogapp.signals  # Importing signals (assuming this file handles signals for the blogapp)


