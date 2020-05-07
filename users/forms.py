from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control bg-custom text-white','placeholder': 'Username..'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control bg-custom text-white','placeholder':'Password..'})
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control bg-custom text-white','placeholder': 'Username..'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control bg-custom text-white','placeholder':'Password..'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control bg-custom text-white','placeholder':'Confirm Password..'})
    )