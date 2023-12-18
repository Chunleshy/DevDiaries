from django import forms
# Defines a form structure for comments in the blog application.
class CommentForm(forms.Form):
     # CommentForm class defines two fields for the comment form.
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