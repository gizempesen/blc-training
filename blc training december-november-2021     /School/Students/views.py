from django.shortcuts import render
from . import models

# Create your views here.
def listStudents(request):
    models.Students.objects.create(name="test", surname="test" , email = "pesengizem@gmail.com" , age = 19, number = 67, grade = 7834)
    return render(request,'list.html', {'data_students': models.Students.objects.all()})