from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    address = models.TextField(max_length=1000)
    summary = models.TextField(max_length=1000)
    degree = models.CharField(max_length=100)    
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.TextField(max_length=100)
    skills= models.TextField(max_length=1000)

    def __str__(self):
        return self.name

