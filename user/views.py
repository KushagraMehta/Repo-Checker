from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # my_dict = {'insert_me': "Hello I am from view.py !"}
    return render(request, 'WELCOME_PAGE\index.html')
