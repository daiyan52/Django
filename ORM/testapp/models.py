from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=32)
    sal = models.IntegerField()
    address = models.CharField(max_length=64)