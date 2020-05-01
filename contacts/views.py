from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from contacts.models import Contact



# @login_required(login_url='/users/login')
@login_required
def index(request):
    # if request.user.is_authenticated:
    user = request.user
    context = {'user': user}
    return render(request, 'contacts/index.html', context)
    
    # return redirect('users/login')

@login_required
def list_contacts(request):
    contacts = Contact.objects.filter(user=request.user.id)

    context = {'contacts': contacts}
    return render(request, 'contacts/list_contact.html', context)

@login_required
def create_contact(request):
    pass