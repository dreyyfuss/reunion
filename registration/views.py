from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.http import HttpResponse

from .forms import UserSignupForm, RegistrationForm
from .utils import send_verification_email
from .tokens import email_verification_token

User = get_user_model()

# Create your views here.
def index(request):
    """
    Render the index page of the registration app.
    """
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        reg_form = RegistrationForm(request.POST)

        if user_form.is_valid() and reg_form.is_valid():
            email = user_form.cleaned_data.get('email')
            password = user_form.cleaned_data.get('password1')

            if User.objects.filter(email=email, is_active=True).exists():
                messages.error(request, "A user with this email already exists.")
                return redirect('register')

            # validate code from reg_form.cleaned_data
            reg_code_obj = reg_form.cleaned_data.get('reg_code_obj')

            try:
                user = User.objects.get(email=email, is_active=False)
                user_form.instance = user
                user = user_form.save(commit=False)
            except User.DoesNotExist:
                user = user_form.save(commit=False)

            user.set_password(password)
            user.is_active = True  # mark active if registration code is valid
            user.save()

            registration = reg_form.save(commit=False)
            registration.user = user
            registration.email = user.email
            registration.save()

            # Handle single-use registration codes
            if reg_code_obj.single_use:
                reg_code_obj.is_active = False
                reg_code_obj.save()

            messages.success(request, "Registration complete. You may now log in.")
            return redirect('login')
        else:
            print("User form: ", user_form.errors)
            print("Reg form: ", reg_form.errors)
            messages.error(request, "Invalid registration data. Check the form error below.")
    else:
        user_form = UserSignupForm()
        reg_form = RegistrationForm()

    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'reg_form': reg_form,
    })
