from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("register/", views.register, name="registration"),
    path("verify-email/<uidb64>/<token>/", views.verify_email, name="verify-email"),
]
