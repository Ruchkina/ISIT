from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Test(models.Model):
    name = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='assets/', blank=True, null=True)

class Performance(models.Model):
    name = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/assets/', blank=True, null=True)





# Create your models here.
