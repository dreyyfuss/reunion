from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name}!")
                return redirect("gallery")
            else:
                messages.error(request, "Please verify your email before logging in.")
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, "users/login.html")


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')