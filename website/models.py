from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    age=models.IntegerField()
    is_Active=models.BooleanField(default=False)