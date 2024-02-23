from django.db import models
from .validators import file_size

# Create your models here.

class videoData(models.Model):
    videoSource = models.CharField(max_length=100, blank=True, null=True)
    videoFile = models.FileField(upload_to='uploads', validators=[file_size])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.videoSource or 'No source'
