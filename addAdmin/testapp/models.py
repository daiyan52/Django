from django.db import models

# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=40)
    dept = models.CharField(max_length=30)