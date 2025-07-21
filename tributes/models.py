from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class DepartedMember(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Tribute(models.Model):
    departed = models.ForeignKey(DepartedMember, on_delete=models.CASCADE, related_name='tributes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tributes')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Tribute by {self.author} for {self.departed}"

    def formatted_date(self):
        return self.created_at.strftime("%A, %b %d")