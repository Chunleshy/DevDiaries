from django.db import models
from django.urls import reverse
from django.conf import settings


# Create your models here.
# Define a Category model
class Category(models.Model):
    title = models.CharField(max_length=25, unique=True)
    class Meta:

        verbose_name_plural = "categories"
    def __str__(self):
        return self.title




# Defining a Python class named Blog that inherits from the models.Model class.
# Django Model 'Blog' representing a blog post.
class Blog(models.Model):
    # Choices for post validity status.
    VALIDITY = [
        ("pending", "pending"),
        ("accepted", "accepted"),
        ("rejected", "rejected")
    ]
    
    # Choices for post status.
    STATUS = [
        ("publish", "PUBLISH"),
        ("draft", "DRAFT")
    ]
    
    # Fields defining the structure of the Blog model.
    title = models.CharField(max_length=50, unique=True)  # Field for the title of the blog post.
    slug = models.SlugField(unique=True)  # Field to store a slug for SEO-friendly URLs.
    body = models.TextField()  # Field for the main content/body of the blog post.
    thumbnail = models.ImageField(upload_to="img", blank=True, null=True)  # Field to store a thumbnail image.
    created = models.DateField(auto_now_add=True, null=True, blank=True)  # Field for creation date.
    updated = models.DateField(auto_now=True, null=True, blank=True)  # Field for last update date.
    status = models.CharField(max_length=20, choices=STATUS, default='draft')  # Field for post status.
    author = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="post", null=True, blank=True)  # Field for the author of the post.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post", null=True, blank=True)  # Field for post category.
    published = models.BooleanField(default=False)  # Field indicating if the post has been published.
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="blog")  # Field to store users who liked the post.
   
    # Method to return a string representation of the Blog instance (using the title).
    def __str__(self):
        return self.title




# Model representing additional user profile information extending the default user model.
class Profile(models.Model):
    
    # List of tuples representing choices for years of experience.
    YEARS_OF_EXPERIENCE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    # Field for a one-to-one relationship with the default user model.
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="my_profile")
    
    # Field to store user's email as an EmailField.
    email = models.EmailField()
    
    # Fields to store user's first name, last name, username, nationality, role, and location.
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    
    # Field to store a user's profile picture, allowing image uploads to the 'p_img' directory.
    picture = models.ImageField(upload_to="p_img", blank=True, null=True)
    
    # Field to store the user's years of experience as an integer field with predefined choices.
    years_of_experience = models.IntegerField(choices=YEARS_OF_EXPERIENCE, blank=True, null=True)
    
    # Fields to store URLs for the user's GitHub, LinkedIn, and Twitter profiles.
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    
    # Field to store a textual biography or description about the user.
    bio = models.TextField(blank=True, null=True)
    
    # Field indicating the proficiency level of the user, defaulted to False.
    proficiency = models.BooleanField(default=False)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="profile")
    # Override the __str__ method to return the username of the associated user.
    def __str__(self):
        return self.user.username

    


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    
    def __str__(self):
        return self.author.username
    









