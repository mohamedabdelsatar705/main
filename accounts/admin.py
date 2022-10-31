from django.contrib import admin
from .models import User,UserSignup
# Register your models here.
admin.site.register(User)
admin.site.register(UserSignup)