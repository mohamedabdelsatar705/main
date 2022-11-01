from pkg_resources import require
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=255,min_length=4,required=True,allow_null=False,allow_blank=False)
    username =serializers.CharField(max_length=30,min_length=4,required=True,allow_null=False,allow_blank=False)
    email = serializers.EmailField(max_length=100,required=False,allow_blank=True ,allow_null=True)
    mobile = serializers.CharField(max_length=11,required=True,allow_blank =False ,allow_null=False)
    date_of_birth = serializers.DateField(required= True,allow_null=False)
    GENDER = [
        ('male', 'male'),
        ('female', 'female'),
    ]
    gender = serializers.ChoiceField(choices=GENDER,required=True,allow_null=False,allow_blank=False)
    password = serializers.CharField(max_length=50,min_length=6,required=True, allow_null=False ,allow_blank =False )
    status = serializers.BooleanField(default=False)
    verified = serializers.BooleanField(default=False)
    type = serializers.BooleanField(default=False)

    class Meta:
        model = User
        fields =["fullname","username","email","mobile","date_of_birth","gender","password","status","verified","type"]

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    def validate_email(self, value):
        if User.objects.filter(email=value).exists() : 
            if value != "":
                raise serializers.ValidationError("A user with this email already exists!")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            if value != "":
                raise serializers.ValidationError("A user with this username already exists!")
        return value

    def validate_mobile(self, value):
        if User.objects.filter(mobile=value).exists() :
            if value != "":
                raise serializers.ValidationError("A user with this mobile already exists!")
        return value
    # def validate(self, attrs):
    #     email_= attrs.get('email', "") 
    #     mobile_= attrs.get('mobile', "")
    #     if mobile_== "" and  email_== "":
    #         raise serializers.ValidationError('Enter email or phone')
    #     return super().validate(attrs)


# class UserSerializer(serializers.Serializer):
#     fullname = serializers.CharField(max_length=255,min_length=4,required=True,allow_null=False,allow_blank=False)
#     username =serializers.CharField(max_length=30,min_length=4,required=True,allow_null=False,allow_blank=False)
#     email = serializers.EmailField(max_length=100,required=False,allow_blank=True ,allow_null=True)
#     mobile = serializers.CharField(max_length=11,required=True,allow_blank =True ,allow_null=False)
#     date_of_birth = serializers.DateField(required= True,allow_null=False)
#     GENDER = [
#         ('male', 'male'),
#         ('female', 'female'),
#     ]
#     gender = serializers.ChoiceField(choices=GENDER,required=True,allow_null=False,allow_blank=False)
#     password = serializers.CharField(max_length=50,min_length=8,allow_null=True)

#     status = serializers.BooleanField(default=False)
#     verified = serializers.BooleanField(default=False)
#     type = serializers.BooleanField(default=False)
      

#     def create(self, validated_data):
#         return User.objects.create(**validated_data)

#     # def validate_email(self, value):
#     #     # lower_email = value.lower()
#     #     if User.objects.filter(email=value).exists() and value != "": 
#     #         raise serializers.ValidationError("A user with this email already exists!")
#     #     return value

#     # def validate_username(self, value):
#     #     if User.objects.filter(username=value).exists():
#     #         raise serializers.ValidationError("A user with this username already exists!")
#     #     return value

#     # def validate_mobile(self, value):
#     #     if User.objects.filter(mobile=value).exists():
#     #         raise serializers.ValidationError("A user with this mobile already exists!")
#     #     return value
#     def validate_email_mobile(self, attrs):
#         email_= attrs.get('email', "") 
#         mobile_= attrs.get('mobile', "")
#         username_= attrs.get('username', "")

#         if mobile_== None and  email_== None:
#             raise serializers.ValidationError('Enter email or phone')
#         if User.objects.filter(email=email_).exists():
#             # if email_ != "": 
#             raise serializers.ValidationError('Email is already in use')

#         if User.objects.filter(mobile=mobile_).exists():
#             # if mobile_ != "":
#             raise serializers.ValidationError('Mobile Number is already in use')

#         if User.objects.filter(username=username_).exists():
#                 raise serializers.ValidationError("A user with this username already exists!")
#         return super().validate(attrs)



    

