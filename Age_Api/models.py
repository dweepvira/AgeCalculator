from msilib.schema import Class
from urllib import request
from django.db import models

# Create your models here.
class Date_details(models.Model):
    Day= models.IntegerField()
    Month = models.IntegerField()
    Year= models.IntegerField()
    
