from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.TextField(max_length=10)
    surname = models.TextField(max_length=10)
    email = models.EmailField(null=True)
    age = models.IntegerField(null=True)
    number = models.IntegerField()
    grade = models.IntegerField()



    def Meta(self):
        db_table = 'Students'
