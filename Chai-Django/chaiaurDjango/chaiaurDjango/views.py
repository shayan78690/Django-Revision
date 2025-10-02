from django.http import HttpResponse # to allow to give response
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at chai aur Django homepage")
    return render(request, 'index.html')

def about(request):
    # return HttpResponse("Hello, world. You are at chai aur Django about page")
    return render(request, 'about.html')

def contact(request):
    # return HttpResponse("Hello, world. You are at chai aur Django contact page")
    return render(request, 'contact.html')