from decimal import Clamped
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Student
from .serializers import Studentserializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class = Studentserializer
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
