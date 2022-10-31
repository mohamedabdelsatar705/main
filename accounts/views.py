from django.shortcuts import render

# Create your views here.
from .models import User
from .serializers import UserSerializer,UserSignupSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view (['GET','POST'])

def loginView (request):
    if request.method == 'POST':
        serializer = UserSignupSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view (['POST'])
def signupStepTow (request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










# {
    
#         "email":"mk@gmail.com",
#         "password":"2345799999"


    

# }
#        "fullname":"duud",
#         "email":"",
#         "username":"vvrjju",
#         "mobile":"01124209090",
#         "date_of_birth":"2000-2-2",
#         "gender":"male"
          