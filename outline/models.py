from django.db import models
from django.db import connection 

# Create your models here.

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute(
        "CREATE DATABASE events"
    )

def make_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)

# add button to use previous startyear, month, day as endyear, month, day
class Event(models.Model):
    # startYear = models.IntegerField(blank = True) 
    # startMonth = models.IntegerField(blank = True)
    # startDay = models.IntegerField(blank = True)
    # startTime = models.DateTimeField()
    startDate = models.DateField()
    startTime = models.TimeField()
    

