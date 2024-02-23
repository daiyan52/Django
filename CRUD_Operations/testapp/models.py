from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll= models.IntegerField()
    student_id = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
