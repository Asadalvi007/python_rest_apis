from rest_framework import serializers
from . models import Departments,Employee
class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Departments
        fields=('DepartmentId','DepartmentName')
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')