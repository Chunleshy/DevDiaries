from django.contrib import admin
from blog.models import Category, Comment, Post

# This section registers the models with their respective admin interfaces to manage them via the Django admin site.

class CategoryAdmin(admin.ModelAdmin):
    # The CategoryAdmin class can contain customizations for the Category model in the admin interface.
    pass

class PostAdmin(admin.ModelAdmin):
    # The PostAdmin class can contain customizations for the Post model in the admin interface.
    pass

class CommentAdmin(admin.ModelAdmin):
    # The CommentAdmin class can contain customizations for the Comment model in the admin interface.
    pass

# Registers the models and their corresponding admin classes for use in the Django admin interface.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
