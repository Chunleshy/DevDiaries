# Importing necessary modules or classes
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget
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
    # ... (other fields omitted for brevity)
    years_of_experience = forms.ChoiceField(choices=YEARS_OF_EXPERIENCE, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Select years of experience"}))
    # ... (other fields omitted for brevity)

    class Meta:
        model = Profile
        exclude = ["user", "proficiency"]

# Define a form to handle Blog Post creation
class PostForm(forms.ModelForm):
    # Define choices for post status
    STATUS = [
        ("draft", "DRAFT"),
        ("publish", "PUBLISH"),
    ]

    # Define various fields with associated HTML attributes for styling and placeholders
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
    body = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder":"Drop a comment here", "rows": 4}))

    class Meta:
        model = Comment
        fields = ["body",]