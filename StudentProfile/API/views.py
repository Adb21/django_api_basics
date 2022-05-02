from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Students
from .serializers import StudentSerializer

# Create your views here.

@api_view(['GET'])
def api_details(request):
    details = {'link 1- To View All Students':'/api/students','link 2- To View Individual Student':'/api/students/<id>','link 3- To Add a Student':'/api/students/add'}
    return Response(details)

@api_view(['GET'])
def students(request):
    stus = Students.objects.all()
    serializer = StudentSerializer(stus,many=True)
    return Response(serializer.data)

@api_view(['GET','DELETE'])
def get_student(request,pk):
    try :
        stus = Students.objects.get(id=pk)
        if request.method == "GET":
            serializer = StudentSerializer(stus,many=False)
            return Response(serializer.data)
        else:
            stus.delete()
            return Response(f"Student id {pk} deleted successfully")

    except Exception as e:
        msg = {'msg':'student not found','error':str(e)}
        return Response(msg)

@api_view(['POST'])
def add_student(request):
    try :
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            msg = {'msg':'student added successfully'}
            return Response(msg)
        msg = {'msg':'student data is not Valid'}
        return Response(msg)
    except Exception as e:
        msg = {'msg':'student creation Failed','error':str(e)}
        return Response(msg)

