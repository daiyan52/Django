from django.db import models

# Create your models here.
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll_no = models.IntegerField()
    dept = models.CharField(max_length=30)
    age  = models.IntegerField()
