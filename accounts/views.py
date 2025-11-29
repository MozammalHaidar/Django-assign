from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib import auth  
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
        else:
            messages.error(request, "Please correct the errors below.")
            return redirect('register')
    form = UserCreationForm()

    context = {
        'form':form
    }
    return render(request,'accounts/register.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('/')
        
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('/')