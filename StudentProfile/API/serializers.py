from dataclasses import fields
from rest_framework import serializers
from .models import Students
from drf_queryfields import QueryFieldsMixin

#QueryFieldsMixin : helps in retriving selected data 
class StudentSerializer(QueryFieldsMixin,serializers.ModelSerializer):
    class Meta :
        model = Students
        fields = '__all__'
        

