from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import ProfileForm
from registration.models import Registration

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

@login_required
def profile_view(request):
    try:
        registration = request.user.registration
    except Registration.DoesNotExist:
        registration = None

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=registration)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.user = request.user
            registration.email = request.user.email
            registration.save()
            messages.success(request, "Your profile has been updated!")
            return redirect('profile')
    else:
        form = ProfileForm(instance=registration)

    return render(request, 'users/profile.html', {
        'form': form,
        'active_tab': 'profile'
    })

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'users/profile.html', {
        'password_form': form,
        'active_tab': 'password'
    })