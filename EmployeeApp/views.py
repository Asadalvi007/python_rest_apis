from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from . models import Departments,Employee
from . serializers import DepartmentsSerializer,EmployeeSerializer
# Create your views here.
@csrf_exempt
def departmentApi(request,id=0):
    if request.method =='GET':
        departments=Departments.objects.all()
        departments_serializer=DepartmentsSerializer(departments,many=True)
        # print(departments_serial)
        return JsonResponse(departments_serializer.data,safe=False)
        # return JsonResponse("Added  departments data successfully",safe=False)

    elif request.method == 'POST':
        department_data= JSONParser().parse(request) 
        departments_serializer=DepartmentsSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added  departments data successfully",safe=False)
        return JsonResponse("Added departments data failed",safe=False)
    elif request.method == 'PUT':
        department_data= JSONParser().parse(request)
        department= Departments.objects.get(DepartmentId=department_data['DepartmentId']) 
        departments_serializer=DepartmentsSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated Data successfully",safe=False)
        return JsonResponse("Data Does not Update",safe=False)
    
    elif request.method == "DELETE":
        department=Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted department data successfully",safe=False)
    else:
        return JsonResponse("Invalid request",safe=False)
        

@csrf_exempt
def employeeApi(request,id=0):
    if request.method =='GET':
        employee=Employee.objects.all()
        employee_serializer=EmployeeSerializer(employee,many=True)
        # print(departments_serial)
        return JsonResponse(employee_serializer.data,safe=False)
        # return JsonResponse("Added  departments data successfully",safe=False)

    elif request.method == 'POST':
        employee_data= JSONParser().parse(request) 
        employee_serializer=EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added  employee data successfully",safe=False)
        return JsonResponse("Added employee data failed",safe=False)
    elif request.method == 'PUT':
        employee_data= JSONParser().parse(request)
        employee= Employee.objects.get(EmployeeId=employee_data['EmployeeId']) 
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Data successfully",safe=False)
        return JsonResponse("Data Does not Update",safe=False)
    
    elif request.method == "DELETE":
        employee=Employee.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Employee data successfully",safe=False)
    else:
        return JsonResponse("Invalid request",safe=False)
        