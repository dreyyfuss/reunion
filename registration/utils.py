from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from .tokens import email_verification_token

def send_verification_email(user, request):
    current_site = get_current_site(request)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = email_verification_token.make_token(user)
    verification_url = reverse("verify-email", kwargs={"uidb64": uid, "token": token})
    full_url = f"http://{current_site.domain}{verification_url}"
    
    subject = "Verify your email address"
    message = f"Hi {user.email},\n\nPlease verify your email by clicking the link below:\n{full_url}\n\nThanks!"
    
    send_mail(subject, message, "noreply@yourdomain.com", [user.email])
