from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def maths(request):
    return render(request,'maths.html')