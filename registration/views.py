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
            password = user_form.cleaned_data.get('password1')  # assuming you're using password1 in your form

            # Check if a user with this email already exists
            if User.objects.filter(email=email, is_active=True).exists():
                messages.error(request, "A user with this email already exists. Please log in or use a different email.")
                return redirect('register')

            # Try to find inactive user with this email
            try:
                user = User.objects.get(email=email, is_active=False)
                # Update user details using the form directly
                user_form.instance = user  # Set the instance to update
                user_form.save()  # Save the updated user

                # Get the registration instance for the user
                registration = user.registration
                # Update registration info using the form directly
                reg_form.instance = registration  # Set the instance to update
                reg_form.save()  # Save the updated registration
            except User.DoesNotExist:
                user = user_form.save(commit=False)
                user.set_password(password)
                user.save()

                # Save registration info
                registration = reg_form.save(commit=False)
                registration.user = user
                registration.email = user.email
                registration.save()

            try:
                send_verification_email(user, request)
                messages.success(request, "Registration complete. Please check your email (including spam) to verify your account.")
            except Exception as e:
                messages.error(request, "There was an error sending the verification email. Please try again.")
                return redirect('register')
            
            return redirect('login')
        else:
            messages.error(request, "Invalid registration data.")
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