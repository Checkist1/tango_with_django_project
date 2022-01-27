from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    res = HttpResponse()
    res.write('Rango says hey there partner!')
    res.write(' <a href="rango/about">About page</a>')
    return res

def about(request):
    res = HttpResponse()
    res.write('Rango says here is the about page.')
    res.write(' <a href="/">Index</a>')
    return res


