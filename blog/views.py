from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'blog/index.html',)

def docu1(request):
    return render(request, 'blog/docu1.html',)

def docu2(request):
    return render(request, 'blog/docu2.html')

def docu3(request):
    return render(request, 'blog/docu3.html',)

def docu4(request):
    return render(request, 'blog/docu4.html',)

def docu5(request):
    return render(request, 'blog/docu5.html',)