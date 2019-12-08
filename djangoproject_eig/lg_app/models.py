from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Myprofileinfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    Profile_site = models.URLField(blank=True)

    Profile_pic = models.ImageField(upload_to='new_app/profile_pic',blank=True)

    def __str__(self):
        return self.user.username