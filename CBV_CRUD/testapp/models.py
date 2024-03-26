from django.db import models
from django.urls import reverse
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32)
    roll = models.CharField(max_length=16)
    address = models.CharField(max_length=64)
    
    def get_absolute_url(self):
        return reverse("StudentDetail", kwargs={"pk": self.pk})
    