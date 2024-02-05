import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FakerModel.settings')
import django
django.setup()
from testapp.models import Student
from faker import Faker
from random import *
from random import randrange
fake = Faker()

def phone():
    d = randrange(6,9)
    num = '+91'+str(d)
    for i in range(9):
        num = num + str(randrange(0,9))
    return num
def generate(n):
    for i in range(n):
        fname = fake.name()
        froll_no = randrange(1,500)
        fmarks = randrange(1,100)
        fdob = fake.date()
        fage = randrange(1,100)
        fdept = fake.random_element(elements=('IT','CSE','ECE','EE','CIVIL','ME'))
        femail = fake.email()
        fphone = phone()
        faddress = fake.address()
        student_record = Student.objects.get_or_create(name=fname,roll_no=froll_no,marks=fmarks,dob=fdob,age=fage,dept=fdept,email=femail,phone=fphone,address=faddress)
n = int(input('Enter the number of students that we have to insert : '))
print(f'{n} records inserted')
generate(n)
