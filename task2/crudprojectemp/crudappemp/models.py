from django.db import models
class Employee(models.Model):
    
    Employee_Id=models.IntegerField()
    Employee_Name=models.CharField(max_length=30)
    Employee_Email=models.CharField(max_length=30)
    Employee_PhoneNumber=models.BigIntegerField()
    Employee_DOB=models.DateField()
    Last_Modified_Date=models.DateField()
