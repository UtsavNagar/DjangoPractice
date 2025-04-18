from django.db import models

# Create your models here.

class Receipe(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)