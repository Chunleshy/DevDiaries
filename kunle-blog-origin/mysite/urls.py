from django.contrib import admin
from django.urls import path, include

# Defines URL patterns for the Django application.

urlpatterns = [
    # Maps the 'admin/' URL to the Django admin site.
    path('admin/', admin.site.urls),

    # Includes URLs from the 'blog' app.
    path("", include("blog.urls")),
]
from django.contrib import admin
from django.urls import path, include

# Defines URL patterns for the Django application.

urlpatterns = [
    # Maps the 'admin/' URL to the Django admin site.
    path('admin/', admin.site.urls),

    # Includes URLs from the 'blog' app.
    path("", include("blog.urls")),
]
