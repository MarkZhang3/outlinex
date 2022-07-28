from django.db import models
from django.db import connection 
from datetime import datetime

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
    event_title = models.TextField()
    start_date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))
    start_time = models.TimeField(default="12:00")

def create_table(table_name):
    with connection.cursor() as cursor:
        query = "CREATE TABLE " + table_name + " ("
        query += """ id INT PRIMARY KEY AUTOINCREMENT,
                event_title TEXT DEFAULT NULL,
                start_date DATE DEFAULT """ + str(datetime.today().strftime('%Y-%m-%d')) + ","
        query += "start_time TIME DEFAULT 12:00)"
        cursor.execute(query)




    

