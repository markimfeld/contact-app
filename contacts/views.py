from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        context = {'user': user}
        return render(request, 'contacts/index.html', context)
    
    return redirect('users/login')
