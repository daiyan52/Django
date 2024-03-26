from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()

    class Meta:
        abstract = True

class Student(Contact):
    
    roll_no = models.IntegerField()
    dept = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}'s profile"

class Teacher(Contact):
    sub = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}'s profile"
