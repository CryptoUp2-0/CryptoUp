from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def faq(request):
    return render(request, 'faq.html')

def our_goals(request):
    return render(request, 'our_goals.html')

def programs(request):
    return render(request, 'programs.html')

from rest_framework import generics
from .models import models  # Замените на вашу модель
from .serializers import YourModelSerializer

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    
    return render(request, 'faq.html', {'form': form})
