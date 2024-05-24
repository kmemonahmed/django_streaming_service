from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/')
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
