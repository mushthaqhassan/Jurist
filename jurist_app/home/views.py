from django.shortcuts import render, redirect   
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Lawyers
from .models import Advocate
from .models import ContactMessage
from django import forms
from django.contrib import auth
from .forms import BookingForm
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

    return render(request, 'contact.html')

def creator(request):
    return render(request, 'mushthaq.html')

def booking(request):
    dict_advocate = {
        'lawyers': Advocate.objects.all()
    }
    return render(request, 'index-lawyer.html', dict_advocate)

def lawyers(request):
    return render(request, 'join_lawyer.html')

def about(request):
    return HttpResponse("About page")

def appointment(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'appointment.html', dict_form)

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser=User.objects.create_user(username,email,password)
        myuser.save
        return redirect('login')
    return render(request, 'signup.html')

def loginn(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
            return HttpResponse("login")

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def registerlawyer(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    form = RegistrationForm()
    dict_form={
        'form': form
    }
    return render(request, 'lawyer_reg.html', dict_form)

def lawlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('lawyers')
    return render(request, 'law_login.html')

def lawsignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        myuser=User.objects.create_user(username,email,password)
        myuser.save
        return redirect('lawlogin')
    return render(request, 'law_signup.html')

def Findcase(request):
    return render(request, 'find_case.html')