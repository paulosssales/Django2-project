from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse


def home(request):
    context = {}
    return render(request, 'news/home.html', context)


def contato(request):
    return HttpResponse("<h1>PÁGINA CONTATO</h1>")
