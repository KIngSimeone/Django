import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from Apptwo.models import User 
from faker import Faker

fakerr = Faker()

def populator(N=5):
    for entry in range(N):

        fake_first = fakerr.first_name()
        fake_last = fakerr.last_name()
        fake_email = fakerr.email()

        
        users = User.objects.get_or_create(first_name=fake_first,last_name=fake_last,email=fake_email)



if __name__== '__main__':
    print("Populating script!")
    populator(25)
    print("Populating Complete")

