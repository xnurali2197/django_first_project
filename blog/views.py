from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, template_name='index.html')

def about(request):
    return render(request, template_name='about.html')

def contact(request):
    return render(request, template_name='contact.html')

def login(request):
    return render(request, template_name='login.html')

def register(request):
    return render(request, template_name='register.html')

def logout(request):
    return render(request, template_name='logout.html')

def profile(request):
    return render(request, template_name='profile.html')