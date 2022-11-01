from django.db import models
class User(models.Model):
    fullname = models.CharField(max_length=255,blank=False,null=False)
    username =models.CharField(max_length=30,blank=False,null=False)
    mobile = models.CharField(max_length=30) 
    email = models.EmailField(max_length=100)

    date_of_birth = models.DateField(null=False)
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    gender = models.CharField(max_length=255,choices=GENDER,blank=False,null=False)
    password = models.CharField(max_length=50)

    status = models.BooleanField(default=False)
    verified = models.BooleanField(default=True)
    type = models.BooleanField(default=False)

    


    def _str__(self):
        return self.email
