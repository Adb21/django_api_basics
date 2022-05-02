import imp
from django.contrib import admin
from .models import Students


# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','marks','city']