from urllib import request
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from Age_Api.serializers import DateSerializers 
from Age_Api.models import Date_details
import requests


class AgeViewSet(viewsets.ModelViewSet):
   queryset = Date_details.objects.all()
   serializer_class = DateSerializers 
   
    

