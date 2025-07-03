from django.db import models


class Registration(models.Model):
    """
    Model to store registration information for the reunion.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    attending = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {'Attending' if self.attending else 'Not Attending'}"