from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        context = {'user': user}
        return render(request, 'contacts/index.html', context)
    
    return render(request, 'users/login.html')
