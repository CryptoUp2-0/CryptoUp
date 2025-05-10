from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def faq(request):
    return render(request, 'faq.html')

def our_goals(request):
    return render(request, 'our_goals.html')

def course(request):
    return render(request, 'course.html')


from rest_framework import generics
from .models import models  
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

from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.contrib import messages

def index(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for your feedback!')
            return redirect('index')
    return render(request, 'index.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("course")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")


