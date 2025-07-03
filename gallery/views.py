from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    Render the index page of the gallery app.
    """
    return render(request, 'gallery/gallery.html')