from django.db import models

# Create your models here.
class Student_Detail(models.Model):
    name=models.CharField(max_length=100)
    college_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)

    def __str__(self):
        return self.name

