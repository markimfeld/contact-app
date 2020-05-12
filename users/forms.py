from django.contrib.auth.models import User
from django.contrib.auth.forms import (
    AuthenticationForm, 
    UserCreationForm, 
    UserChangeForm,
    PasswordChangeForm,
)
from django import forms


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class':'form-control bg-custom text-white',
                'placeholder': 'Username..'
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control bg-custom text-white',
                'placeholder':'Password..'
            }
        )
    )

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class':'form-control bg-custom text-white',
                'placeholder': 'Username..'
            }
        )
    )
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control bg-custom text-white',
                'placeholder':'Password..'
            }
        )
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control bg-custom text-white',
                'placeholder':'Confirm Password..'
            }
        )
    )

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Username..',
                'class': 'form-control bg-custom text-white rounded',
            }
        )
    )
    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'First name..',
                'class': 'form-control bg-custom text-white rounded',
            }
        )
    )
    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Last name..',
                'class': 'form-control bg-custom text-white rounded',
            }
        )
    )
    email = forms.EmailField(
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Email..',
                'class': 'form-control bg-custom text-white rounded',
            }
        )
    )
        
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update(
            {'placeholder': 'Old Password..', 'class': 'form-control bg-custom text-white rounded'}
        )
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control bg-custom text-white rounded', 'placeholder': 'New Password..'}
        )
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control bg-custom text-white rounded', 'placeholder': 'Confirm New Password..'}
        )