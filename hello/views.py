from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import bleach
import  requests

# from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def scraper(request):
    return render(request, 'scraper.py')
# def db(request):

#     greeting = Greeting()
#     greeting.save()

#     greetings = Greeting.objects.all()

#     return render(request, 'db.html', {'greetings': greetings})

