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
            user = user_form.save()
            registration = reg_form.save(commit=False)
            registration.user = user
            registration.email = user.email
            registration.save()

            send_verification_email(user, request)

            messages.success(request, "Registration complete. Please check your email to verify your account.")
            return redirect('login')
    else:
        user_form = UserSignupForm()
        reg_form = RegistrationForm()

    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'reg_form': reg_form,
    })


def verify_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and email_verification_token.check_token(user, token):
        user.is_active = True
        user.save()
        # Redirect to success page or login
        return redirect("login")
    else:
        return HttpResponse("Email verification failed")