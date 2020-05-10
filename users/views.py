from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from .forms import (
    CustomAuthForm, 
    CustomUserCreationForm, 
    CustomUserChangeForm,
    CustomPasswordChangeForm,
)
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import (
    UserCreationForm, 
    PasswordChangeForm,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
import datetime


date = datetime.date.today

# Create your views here.

def register(request):
    if not request.user.is_authenticated:    
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(data=request.POST)
            if form.is_valid():
                user = form.save()

                if user is not None:
                    do_login(request, user)

                    return redirect('/profile')

        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None

        return render(request, 'users/register.html', {'form': form, 'date': date})
    else:
        return redirect('/profile')

def login(request):

    if not request.user.is_authenticated:
        form = CustomAuthForm()
        if request.method == 'POST':
            # add data to the form
            form = CustomAuthForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username, password=password)

                if user is not None:
                    do_login(request, user)

                    return redirect('/profile')

        return render(request, 'users/login.html', {'form': form, 'date': date})
    else:
        return redirect("/profile")

@login_required
def logout(request):
    # finish session
    do_logout(request)
    return redirect('/users/login')

@login_required
def edit_user(request):

    form = CustomUserChangeForm()

    if request.method == 'POST':
        form = CustomUserChangeForm(data=request.POST, instance=request.user)

        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your profile have been edited successfully!')

            if user is not None:
                return redirect('/profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
            

    context = {'form': form, 'date': date}
    return render(request, 'users/edit_user.html', context)

@login_required
def password_change(request):

    if request.method == 'POST':
        form = CustomPasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            new_password = form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password has been changed successfully!')

            if new_password is not None:
                return redirect('/profile')
    else:
        form = CustomPasswordChangeForm(user=request.user)

    context = {'form': form, 'date': date}

    return render(request, 'users/change_password.html', context)