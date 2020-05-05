from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
# from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomAuthForm, CustomUserCreationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
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