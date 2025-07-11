from django.urls import path
from . import views

urlpatterns = [
    path("gallery/", views.gallery, name="gallery"),
    path("photo/upload/", views.upload_photo, name="upload_photo"),
    path("photo/<int:pk>/", views.photo_detail, name="photo_detail"),
]