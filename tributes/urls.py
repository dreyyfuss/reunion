from django.urls import path
from . import views

urlpatterns = [
    path('tributes/', views.tribute_list, name='tribute_list'),
    path('tributes/create/', views.create_tribute, name='create_tribute'),
]