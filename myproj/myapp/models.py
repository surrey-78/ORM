from django.db import models
from django.contrib import admin

# Create your models here.
class Employee(models.Model):
    emp_id=models.CharField(primary_key=True,max_length=6,help_text="Employee ID")
    ename=models.CharField(max_length=50)
    post=models.CharField(max_length=20)
    salary=models.IntegerField()
    age=models.IntegerField()
    

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('emp_id','ename','post','salary','age')
    
