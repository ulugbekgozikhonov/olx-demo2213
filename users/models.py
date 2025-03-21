from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    GENDER_TYPE = (
        ('Male', 'male'),
        ('Female', 'female'),
    )
    
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to="users/image/",null=True, blank=True)
    gender = models.CharField(choices=GENDER_TYPE,null=True, blank=True, max_length=7)
    phone_number = models.CharField(max_length=15)

    