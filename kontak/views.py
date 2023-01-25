from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")

def about(request):
    return HttpResponse("<p>Hello, this is about.</p>")

def Home(request):
    context = {
        'nama' : 'hello',
    }
    return render(request, 'pkl/home.html', context)