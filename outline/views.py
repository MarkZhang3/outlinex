from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import connection
from datetime import datetime, date, time
from .models import Table
from .models import Event 
import calendar 

# Create your views here.

def index(request):
    content = {
        'tables': Table.objects.all()
    }
    return render(request, 'index.html', content)

def add_event(request):
    temp = str(datetime.today().strftime('%Y-%m-%d'))
    content = {
        'cur_date': temp
    }
    return render(request, 'add_event.html', content)

def add_event_to_record(request):
    if request.method == 'POST':
        table = str(request.POST.get('table')) 
        sd = list(map(int, request.POST.get('start_date').split('-')))
        st = list(map(int, request.POST.get('start_time').split(':')))
        ed = list(map(int, request.POST.get('end_date').split('-')))
        et = list(map(int, request.POST.get('end_time').split(':')))
        t = Table.objects.filter(name=table)[0] # there may be multiple tables with the same name
        e = Event.objects.create(
            table=t,
            text = request.POST.get('event_text'),
            start_date = date(sd[0], sd[1], sd[2]),
            start_time = time(st[0], st[1]),
            end_date = date(ed[0], ed[1], ed[2]),
            end_time = time(et[0], et[1]),
            completed = False
        )


def sort_by_start_date(request):
    if request.method == 'POST':
     # select * from <table>.event_set.all() order by start_date, start_time
        table_name = request.POST.get('table')
        table = Table.objects.get(name=table_name)
        events = table.event_set.all().order_by('start_date', 'start_time')
        return render(request, 'index.html')

def filter_title(request):
    filter = request.POST('filter_title')

def add_table(request):
    return render(request, 'add_table.html')

def add_table_to_record(request):
    if request.method == 'POST':
        table_name = str(request.POST.get('table_name'))
        t = Table(name=table_name)
        t.save()
        return index(request)

def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    table = event.table
    table.event_set.remove(event)
    event.delete()
    return HttpResponseRedirect('index.html')