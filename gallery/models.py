from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Photo(models.Model):
    """
    Model to store photos for the reunion gallery.
    """
    image = models.ImageField(upload_to='photos/')
    user = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE, related_name="photos")
    caption = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model to store comments on photos in the gallery.
    """
    user = models.ForeignKey(to=User, null=True, on_delete=models.CASCADE, related_name='comments')
    photo = models.ForeignKey(to=Photo, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.text[:20]}..."  # Display first 20 characters of the comment