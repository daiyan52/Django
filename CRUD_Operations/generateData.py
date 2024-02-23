import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRUD_Operations.settings')

import django
django.setup()

from testapp.models import Student

from faker import Faker
import random
def data(n):
    for i in range(n):
        fake = Faker()
        name = fake.name()
        roll = random.randint(4304200100001,4304200100120)
        address = random.choice([
            'West Bengal', 'Bihar', 'Uttar Pradesh', 'Jharkhand'
        ])
        student_id = 'NIT/2020/0'+str(random.randint(100,900))
        student_record = Student.objects.get_or_create(name=name,roll=roll,address=address,student_id=student_id)
print('Enter the No of Fields that you want to inspect')
n = int(input())
data(n)
print(f'{n} fields are inserted into the database')