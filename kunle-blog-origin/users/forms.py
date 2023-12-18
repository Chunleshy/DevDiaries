from django import forms

# Defines a form structure for user login.

class LoginForm(forms.Form):
    # LoginForm class defines fields for username and password.
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
