from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """
    Render the index page of the registration app.
    """
    return render(request, 'home.html')


def registration(request):
    """
    Render the registration page of the registration app.
    """
    if request.method == 'POST':
        # Handle form submission here
        # For example, you might save the registration data to the database
        pass

    else:
        return render(request, 'registration/registration.html')