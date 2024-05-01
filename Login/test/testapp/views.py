from django.shortcuts import render
from django.http import HttpResponse
def home(request):
     searchTerm = request.GET.get('searchMovie')
     return render(request, 'home.html', {'searchTerm':searchTerm})
def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})
def about(request):
     return HttpResponse ('<h1>welcome to about page<h1>')
# Create your views here.
