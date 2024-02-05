#estd = models.DateField()
#    company = models.CharField(max_length=100)
#    position = models.CharField(max_length=100)
#    eligibility = models.CharField(max_length=100)
#    location = models.CharField(max_length=100)
#    email = models.EmailField()
#    phone = models.BigIntegerField()

print('hello')
from faker import Faker
fake = Faker()
name = fake.name()
print(name)
