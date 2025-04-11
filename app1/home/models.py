from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField(upload_to='student_images/', null = True, blank = True)  # Recommended to set upload_to
    file = models.FileField(upload_to='student_files/')     # Recommended to set upload_to
    
    
class Car(models.Model):
    name = models.CharField(max_length=40)
    speed = models.IntegerField(default=50)
    
    def __str__(self) -> str:
        return self.name   