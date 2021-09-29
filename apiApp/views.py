from functools import partial
from apiApp.serializers import StudentSerializer
from apiApp.models import Student
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
import io
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def student_api(request):
    if request.method=='GET':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')

        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    elif request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            msg = {
                'msg':'Student Created'
            }

            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    elif request.method=='PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        stu_id = python_data.get('id')
        stu = Student.objects.get(id=stu_id)
        # If we don't mention partial=True the serilizer will expect all the values to be passed and will thorow an error if not passed.
        serializer = StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg = {
                'msg':'Student Updated'
            }

            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    elif request.method=='DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        stu_id = python_data.get('id')
        stu_data = Student.objects.get(id=stu_id)
        stu_data.delete()
        msg = {
                'msg':'Student Deleted'
            }

        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')




