from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    roll_no = models.IntegerField()
    marks = models.IntegerField()
    dob = models.DateField()
    age = models.IntegerField()
    dept = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    address = models.TextField(max_length=100)