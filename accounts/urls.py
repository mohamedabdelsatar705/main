from django.urls import path
from . import views

urlpatterns = [
    path('loginView/',views.loginView),
    path('signupStepTow/',views.signupStepTow),
    
]