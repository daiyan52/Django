import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','modelproject.settings')
import django
django.setup()

from testapp.models import Student
from faker import Faker
from random import *
fake = Faker()

def populate(n):
     for i in range(n):
        fname = fake.name()
        froll_no = fake.random_int(min=1,max=999)
        fdept = fake.random_element(elements=('IT','CSE','EE','ECE','CIVIL','ME'))
        fage = fake.random_int(min=22,max=30)
        student_record = Student.objects.get_or_create(name=fname,roll_no=froll_no,dept=fdept,age=fage)
n = int(input('Enter Number of Record which you want to Insert :  '))
print(f'{n} recored are inserted Successfully')  
populate(n)