from django.shortcuts import render
import io
import logging
from rest_framework.parsers import JSONParser
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def get_employee(request):

    if request.method == 'GET':
        json_data = request.body
        logging.info(f"JSON Data: {json_data}")   
        stream = io.BytesIO(json_data)
        logging.info(f"Stream Data: {stream}")
        pythondata = JSONParser().parse(stream)
        logging.info(f"PythonData: {pythondata}")
        id = pythondata.get('id', None)

        if 'id' is not None:
            emp = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(emp)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')
    
@csrf_exempt
def insert_employee(request):
    
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            response = {'error':False,'msg':'Employee Record Inserted'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
    
@csrf_exempt
def update_employee(request):
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        emp = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(emp, data=pythondata, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            response = {'error':False,'msg':'Employee Record Updated'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def delete_employee(request):
    
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        emp = Employee.objects.get(id=id)
        emp.delete()
        response = {'error':False,'msg':'Employee Record Deleted'}
        json_data = JSONRenderer().render(response)
        return HttpResponse(json_data, content_type='application/json')
    
