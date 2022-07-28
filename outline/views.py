from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import connection
from datetime import datetime
from .models import Events
from .models import create_table
import calendar 

# Create your views here.

def index(request):
    cursor = connection.cursor()
    all_tables = cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
    content = {}
    for table in all_tables:
        content[str(table)] = cursor.execute("SELECT * FROM "+str(table))
    return render(request, 'index.html')

def add_event(request):
    temp = str(datetime.today().strftime('%Y-%m-%d'))
    content = {
        'cur_date': temp
    }
    return render(request, 'add_event.html', content)

def add_event_to_record(request):
    if request.method == 'POST':
        table = str(request.POST.get('table'))
        event_title = request.POST.get('title')
        start_date = request.POST.get('start_date')
        start_time = request.POST.get('start_time')
        end_date = request.POST.get('end_date')
        end_time = request.POST.get('end_time')
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO "+table+" VALUES ("+event_title+","+start_date+","+start_time+","+end_date+","+end_time
        )
    

def sort_by_date(request):
    content = {
        "all_events": Events.objects.raw("SELECT * FROM Events ORDER BY start_date ASC")
    }
    return render(request, 'index.html', content)

def filter_title(request):
    filter = request.POST('filter_title')

def add_table(request):
    if request.method == 'POST':
        table_name = str(request.POST.get('table_name'))
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE " + table_name + " ("
        )