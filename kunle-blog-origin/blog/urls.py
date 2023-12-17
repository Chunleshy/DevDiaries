from django.urls import path
from . import views

# These URL patterns define the mapping between URLs and views in the Django application.

urlpatterns = [
    # Maps the root URL to the blog_index view.
    path("", views.blog_index, name="blog_index"),

    # Maps URLs with the pattern 'post/<int:pk>/' to the blog_detail view.
    # '<int:pk>' is a placeholder for the primary key of a post.
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),

    # Maps URLs with the pattern 'category/<category>/' to the blog_category view.
    # '<category>' is a placeholder for the category name.
    path("category/<category>/", views.blog_category, name="blog_category"),
]
