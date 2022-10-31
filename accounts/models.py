from django.db import models

class UserSignup(models.Model):
    email = models.EmailField(max_length=100,null=True ,blank=True)
    mobile = models.DecimalField(max_digits=10, decimal_places=0,null=False)  
    password = models.CharField(max_length=50)
    
    def _str__(self):
        return self.email

class User(models.Model):
    fullname = models.CharField(max_length=255,blank=False,null=False)
    email = models.EmailField(max_length=100)
    username =models.CharField(max_length=30,blank=False,null=False)
    mobile = models.DecimalField(max_digits=10, decimal_places=0,null=False)  
    date_of_birth = models.DateField(null=False)
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    gender = models.CharField(max_length=255,choices=GENDER,blank=False,null=False)
    status = models.BooleanField(default=False)
    verified = models.BooleanField(default=True)
    type = models.BooleanField(default=False)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIEDS = ['mobile', 'full_name','status']  
    #comment



    def _str__(self):
        return self.email
