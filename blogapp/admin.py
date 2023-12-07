from django.contrib import admin
from .models import Blog, Profile, Category, Comment
from django_summernote.admin import SummernoteModelAdmin 

# Register your models here.

# Creating a class BlogAdmin that inherits from SummernoteModelAdmin
class BlogAdmin(SummernoteModelAdmin):
    # Define the fields to be displayed in the admin panel for Blog model
    list_display = ["title", "author", "category", "status", "published"]
    
    # Enable filtering by 'status' field in the admin panel for Blog model
    list_filter = ("status", )
    
    # Enable search functionality for 'title' and 'body' fields in the admin panel for Blog model
    search_fields = ['title', 'body']
    
    # Automatically populate the 'slug' field based on the 'title' field in the admin panel for Blog model
    prepopulated_fields = {"slug": ("title",)}
    
    # Define which fields will use the Summernote rich text editor in the admin panel for Blog model
    summernote_fields = ('body', ) 

# Customize the site header for the Django administration panel
admin.site.site_header = "DevDiaries Administration"

# Registering the models and their respective admin classes to be managed via the Django admin panel
admin.site.register(Blog, BlogAdmin)
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Comment)

