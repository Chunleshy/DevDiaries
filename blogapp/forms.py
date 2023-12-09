# Importing necessary modules or classes
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.contrib.auth import get_user_model
from .models import Profile, Blog, Category, Comment

# Define a custom registration form that inherits from UserCreationForm
class RegisterForm(UserCreationForm):
    # Define form fields with associated HTML attributes for styling and placeholders
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email address"})
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"})
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"})
    )

    # Define metadata for the form, specifying the model and fields to include
    class Meta:
        # Use the custom user model defined in the project
        model = get_user_model()
        # Specify the fields to include in the form
        fields = ["username", "email", "password1", "password2"]

# Define a form to handle Profile information
class ProfileForm(forms.ModelForm):
    # Define choices for years of experience
    YEARS_OF_EXPERIENCE = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    # Define various fields with associated HTML attributes for styling and placeholders
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email address"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter firstname"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter lasttname"}))
    picture = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "upload image"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Describe yourself"}))
    location = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Omaha, Nebraska"}))
    nationality = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"USA"}))
    role = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Aspiring FullStack Developer"}))
    years_of_experience = forms.ChoiceField(choices=YEARS_OF_EXPERIENCE, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Select years of experience"}))
    # enter social media links
    github_url = forms.URLField(required=False, widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter github_url"}))
    linkedin_url = forms.URLField(required=False, widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter linkedin_url"}))
    twitter_url = forms.URLField(required=False, widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter twitter_url"}))

    class Meta:
        model = Profile
        exclude = ["user", "proficiency", "follow"]

# Define a form to handle Blog Post creation
class PostForm(forms.ModelForm):
    # Define choices for post status
    STATUS = [
        ("draft", "DRAFT"),
        ("publish", "PUBLISH"),
    ]

    # Define various fields with associated HTML attributes for styling and placeholders to create an article
    title = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", "placeholder": "Enter post title"}))
    body = forms.CharField(widget=SummernoteWidget())  # Using Summernote widget for rich text input
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "upload image"}))
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select(attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select', "placeholder": "Choose a category"})
    )

    class Meta:
        model = Blog
        fields = ["title", "body", "thumbnail", "status", "category"]

# Define a form to handle Comments
class CommentForm(forms.ModelForm):
    # Define a field for comment body with associated HTML attributes for styling and placeholders
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Drop your comment here", "rows": 4}))

    class Meta:
        model = Comment
        fields = ["body",]