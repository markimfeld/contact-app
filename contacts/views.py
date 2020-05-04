from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from contacts.models import Contact
from contacts.forms import ContactForm
import datetime

date = datetime.date.today

def is_valid_queryparam(param):
    return param != '' and param is not None



def index(request):
    return render(request, 'contacts/index.html', {})

# @login_required(login_url='/users/login')
@login_required
def profile(request):
    
    # if request.user.is_authenticated:
    user = request.user
    context = {'user': user, 'date': date}
    return render(request, 'contacts/profile.html', context)
    
    # return redirect('users/login')

@login_required
def list_contacts(request):
    contacts = Contact.objects.filter(user=request.user.id)
    categories = ['FR', 'FY', 'CO', 'OR']
    category = request.GET.get('category')

    if is_valid_queryparam(category) and category != 'Choose...':
        contacts = contacts.filter(category=category)

    context = {
        'contacts': contacts, 
        'date': date,
        'categories': categories
    }
    return render(request, 'contacts/list_contact.html', context)

@login_required
def detail_contact(request, pk):
    
    contact = Contact.objects.filter(user=request.user.id).get(pk=pk)

    context = {
        'contact': contact,
        'date': date
    }

    return render(request, 'contacts/detail_contact.html', context)

@login_required
def create_contact(request):

    form = ContactForm()

    if request.method == 'POST':
        
        form = ContactForm(request.POST, request.FILES)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()

            if contact is not None:
                return redirect('/contacts')
    else:
        form = ContactForm()

    context = {'form': form, 'date': date}

    return render(request, 'contacts/create_contact.html', context)

@login_required
def edit_contact(request, pk):
    
    contact = Contact.objects.get(pk=pk)

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()

            if contact is not None:
                return redirect('/contacts')
    else:
        # with this we put the data that has the old contact
        form = ContactForm(instance=contact)
    
    context = {'form': form, 'date': date}

    return render(request, 'contacts/edit_contact.html', context)

@login_required
def delete_contact(request, pk):
    
    contact = Contact.objects.get(pk=pk)

    if contact is not None:
        contact.delete()

    # return render(request, 'contacts/list_contact.html', {})
    return redirect('/contacts')

