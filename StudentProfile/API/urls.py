"""StudentProfile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from . import views
from django.urls import path,include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),

    # path('', views.api_details,name='api_details'),
    # path('students/', views.students,name='students'),
    # path('students/<int:pk>', views.get_student,name='get_student'),
    # path('students/add', views.add_student,name='add_student'),
]