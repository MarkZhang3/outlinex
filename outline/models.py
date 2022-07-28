from django.db import models
from django.db import connection 
from datetime import datetime

# Create your models here.

class Table(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name 
    

class Event(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    text = models.TextField()
    start_date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    completed = models.BooleanField()

    def __str__(self):
        return self.text






    

