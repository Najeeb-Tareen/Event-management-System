from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length= 120)
    date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=100)

    


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class Person(models.Model):
    f_name =  models.CharField(max_length= 64)
    email =  models.CharField(max_length= 64)
    password =  models.CharField(max_length= 64)


class Team(models.Model):
    name = models.CharField(max_length= 128)
    owner = models.CharField(max_length= 128)
    rank = models.CharField(max_length= 128)
