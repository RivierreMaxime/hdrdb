from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Bienvenue dans ton crud !")

def test(request):
    return HttpResponse("Ceci est un test")

#https://www.javatpoint.com/django-crud-example