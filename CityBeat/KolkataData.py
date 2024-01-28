import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CityBeat.settings')


import django
django.setup()

from testapp.models import Kolkata_job

from faker import Faker
import random
fake = Faker()

def phone():
    d = fake.random.randint(6, 9)
    num = str(d)
    for i in range(9):
        num = num + str(random.randint(0, 9))
    return int(num) 


def generate(n):
    for i in range(n):
        festd = fake.date()
        fcompany = fake.company()
        fposition = fake.random_element(elements=('Software Developer/Engineer',
                                         'Database Administrator',
                                         'Project Manager',
                                         'Quality Assurance (QA) Analyst',
                                         'Data Scientist',
                                         'DevOps Engineer'
))
        feligibility = fake.random_element(elements=('B.Tech','M.Tech','MCA','BCA'))
        flocation = fake.address()
        femail = fake.email()
        fphone = phone()
        jobs_reocrd = Kolkata_job.objects.get_or_create(estd=festd,
                                                        company=fcompany,
                                                        position=fposition,
                                                        eligibility=feligibility,
                                                        location=flocation,
                                                        email=femail,
                                                        phone=fphone)

n = int(input('Enter the number of required Field : '))   
generate(n)
print(f'{n} Fiends are inserted successfully')