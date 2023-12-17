from django.contrib import admin
from blog.models import Category, Comment, Post

# These classes and registrations configure how the models are displayed in the Django admin interface.

class CategoryAdmin(admin.ModelAdmin):
    # Customizes the display of Category models in the admin interface.
    pass

class PostAdmin(admin.ModelAdmin):
    # Customizes the display of Post models in the admin interface.
    pass

class CommentAdmin(admin.ModelAdmin):
    # Customizes the display of Comment models in the admin interface.
    pass

# Registers the models and their corresponding admin customizations.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
