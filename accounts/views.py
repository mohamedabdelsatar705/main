from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view (['POST'])
def signup (request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)   
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# @api_view (['POST'])
# def signupStepTwo (request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data=request.data)   
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else :
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
