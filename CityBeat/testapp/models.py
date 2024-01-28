from django.db import models

# Create your models here.
class Kolkata_job(models.Model):
    estd = models.DateField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()


class Delhi_job(models.Model):
    estd = models.DateField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()



class Bengaluru_job(models.Model):
    estd = models.DateField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()

class Hyderabad_job(models.Model):
    estd = models.DateField()
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField()

