from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website1/about.html')

def contact(request):
    return render(request,'website2/contact.html')

