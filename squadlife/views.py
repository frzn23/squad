from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gal(request):
    return render(request, 'gallery.htm')

def contact(request):
    return render(request, 'contact.htm')