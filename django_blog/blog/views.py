from django.contrib.auth.forms import login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

# User Registration
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            form = CustomUserCreationForm()
            return render(request, "blog/register.html", {"form":form})
    
# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home") # Redirect to homepage after login
        else:
            form = AuthenticationForm()
            return render(request, "blog/login.html", {"form":form})
        
# User Logout 
def user_logout(request):
    logout(request)
    return redirect("login")

# User Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get("email")
        user.save()
        return redirect("profile")
    return render(request, "blog/profile.html")
