from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

from .choices import SHIRT_SIZES, CURRENCY_CHOICES


User = get_user_model()

class Registration(models.Model):
    """
    Model to store registration information for the reunion.
    """
    user = models.OneToOneField(to=User, null=True, on_delete=models.CASCADE, related_name='registration')
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address_line_1 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = CountryField(null=True, blank=True)
    shirt_size = models.CharField(max_length=10, choices=SHIRT_SIZES, null=False, default='M')
    gift1 = models.URLField(null=True, blank=True)
    gift2 = models.URLField(null=True, blank=True)
    gift3 = models.URLField(null=True, blank=True)
    gift4 = models.URLField(null=True, blank=True)
    donation_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, null=True, blank=True )
    donation_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"