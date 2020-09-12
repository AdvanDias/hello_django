from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request, nome):
    return HttpResponse('<h1>Hello {}<h1>'.format(nome))