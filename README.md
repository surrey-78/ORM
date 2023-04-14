# Ex02 Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a student database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![ErDiagram](https://user-images.githubusercontent.com/119559366/232076998-5a3072df-440a-47f4-a930-f5c99e4b7cae.png)


## DESIGN STEPS

### STEP 1:
Create a django application using django-admin startapp <appname> in command line.
Head to the application directory created inside the project directory. Open the models.py file.
In models.py create two classes one defining the attributes and the other one defining attribute value types.
### STEP 2:
In the same directory, Head to admins.py and import the two classes from models.py that you have created earlier.
Now register your created models in admins.py file and save both the files.
### STEP 3:
Start the Django server and head over to admin page.
Using the admin interface, you can add or delete data in the database.

## PROGRAM
```
File: Models.py

from django.db import models
from django.contrib import admin

class Employee (models.Model):
    unique_number=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    job=models.CharField(max_length=100)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('unique_number','name','age','email','job')

File: Admin.py

from django.contrib import admin
from .models import Employee,EmployeeAdmin

admin.site.register(Employee,EmployeeAdmin)
```

## OUTPUT

![djOutput](https://user-images.githubusercontent.com/119559366/232080061-2cb73937-ed19-4faa-97c9-7d78dcf55dec.png)


## RESULT
A Django application has been created that can be used to store and retrieve data from the database using Object Relational Mapping(ORM).
