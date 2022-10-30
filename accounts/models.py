from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class User(models.Model):
    fullname = models.CharField(max_length=255,blank =False ,null=False)
    email = models.EmailField(max_length=100, unique=True)
    username =models.CharField(max_length=30,null=False)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11, validators=[phone_validator], unique=True)
    date_of_birth = models.DateField(null=True)
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    gender = models.CharField(max_length=255,choices=GENDER, blank=True,null=True)
    status = models.BooleanField(default=False)
    verified = models.BooleanField(default=True)
    type = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIEDS = ['email', 'full_name']

def _str__(self):
    return self.email
