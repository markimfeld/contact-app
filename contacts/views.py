from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    user = request.user
    context = {'user': user}
    return render(request, 'contacts/index.html', context)


def login(request):
    pass

def register(request):
    pass