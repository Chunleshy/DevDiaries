from django import forms

# This form class defines the structure of the comment form for the blog application.

class CommentForm(forms.Form):
    # Represents the structure of the comment form fields.
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your Name"}
        ),
    )
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Leave a comment!"}
        )
    )
