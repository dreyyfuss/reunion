from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="home"),
    path("/register", views.registration, name="registration"),
]
