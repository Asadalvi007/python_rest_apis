from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=300)
class Employee(models.Model):
    EmployeeId=models.AutoField(primary_key=True)
    EmployeeName=models.CharField(max_length=500)
    Department=models.CharField(max_length=500)
    DateOfJoining=models.DateTimeField()
    PhotoFileName=models.CharField(max_length=500)
class customer(models.Model):
    CustomerId=models.AutoField(primary_key=True)
    CustomerName=models.CharField(max_length=500)
    CustomerLocation=models.CharField(max_length=500)
    CustomerNumber=models.CharField(max_length=500)