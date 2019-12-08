import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','DjangoProj.settings')

import django
django.setup()

import random
from D_App.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):

	for entry in range(N):

		fake_name = fakegen.name().split()
		faker_first_name = fake_name[0]
		faker_last_name = fake_name[1]
		fake_email = fakegen.email()

		user_info = User.objects.get_or_create(First_Name=faker_first_name,Last_Name=faker_last_name,Email=fake_email)[0]

if __name__=='__main__':
	print('populating script')
	populate(20)
	print('Populating Completed')