from django.db import models

# Create your models here.

class Photo(models.Model):
    """
    Model to store photos for the reunion gallery.
    """
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    photo_author = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    Model to store comments on photos in the gallery.
    """
    photo = models.ForeignKey(Photo, related_name='comments', on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=100, null=False)
    comment_author_email = models.EmailField(null=False)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} - {self.text[:20]}..."  # Display first 20 characters of the comment