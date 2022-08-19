from contextlib import nullcontext
from django.db import models
from django.db import connection 
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Table(models.Model):
    name = models.TextField()
    user = models.TextField() # using ForgienKey raises errors because there is no column for user_id
    #   value will be assigned in views.py upon creation since each user has a unique username

    def __str__(self):
        return self.name 
    

class Event(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    text = models.TextField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    completed = models.BooleanField()

    def __str__(self):
        return self.text

class User(User):
    email_password = models.TextField(null=True, default="")

    def __str__(self):
        return User.username

    

