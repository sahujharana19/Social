from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    platform = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)
