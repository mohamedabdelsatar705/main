


from pkg_resources import require
from rest_framework import serializers
from .models import User 
from django.core.validators import RegexValidator


# Create your models here.
phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$", "The phone number provided is invalid")


class UserSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=255,allow_blank =False ,allow_null=False)
    email = serializers.EmailField(max_length=100,required=False ,allow_blank=True)
    username =serializers.CharField(max_length=30,allow_null=False)
    password = serializers.CharField(max_length=50,min_length=8)
    mobile = serializers.CharField(max_length=11, validators=[phone_validator],allow_blank =False ,allow_null=False)
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    gender = serializers.ChoiceField(choices=GENDER, allow_blank=True,allow_null=True)
    status = serializers.BooleanField(default=False)
    verified = serializers.BooleanField(default=False)
    type = serializers.BooleanField(default=False)

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIEDS = ['email', 'full_name']

    def create(self, validated_data):
        return User.objects.create(**validated_data)


    def validate(self, attrs):

        mobile_ = attrs.get('mobile', '')
        email_ = attrs.get('email', '') # get - Provide defualt param is email not inserted
        # password_ = attrs.get('password', '')
        
        if mobile_ == '' and  email_== '':
            raise serializers.ValidationError('Enter email or phone')

        elif User.objects.filter(email=email_).exists():
            if email_ != '': 
                raise serializers.ValidationError(
                {'email',('Email is already in use')})

        elif User.objects.filter(mobile=mobile_).exists():
            if mobile_ != '':
                raise serializers.ValidationError(
                {'mobile',('Phone Number is already in use')})
                
        # elif User.objects.filter(username=username_).exists():
        #     raise serializers.ValidationError(
        #         {'username',('Username is already in use')})

        return super().validate(attrs)