import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ORM.settings')
import django

django.setup()
from testapp.models import Employee
from faker import Faker
from random import randint
fake = Faker()

def generate_data(n):
    for i in range(n):
        fname = fake.name()
        fsal = randint(25000,75000)
        faddress = fake.city()
        record = Employee.objects.get_or_create(name=fname, sal=fsal, address=faddress)
n = int(input('Enter the number of employees that we have to insert : '))
print(f'{n} records inserted')
generate_data(120)
        