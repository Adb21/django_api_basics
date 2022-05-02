from msilib.schema import Class
from turtle import mode
from django.db import models

# Create your models here.

class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    marks = models.IntegerField(max_length=3)
    city = models.CharField(max_length=30)


