from django.shortcuts import render
from django.http import HttpResponse
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
        return index(request)

def add_table(request):
    return render(request, 'add_table.html')

def add_table_to_record(request):
    if request.method == 'POST':
        table_name = str(request.POST.get('table_name'))
        t = Table(name=table_name)
        t.save()
        return index(request)

def delete_event(request, id):
    event = Event.objects.get(id=id)
    event.delete()
    return index(request)

def details(request, id):
    event = Event.objects.get(id=id)
    content = {}
    content['event'] = event 
    return render(request, 'details.html', content)

def update_event(request, id):
    event = Event.objects.get(id=id)
    changeList = request.POST
    if changeList['event_text'] != '':
        event.text = changeList['event_text']
    if changeList['start_date'] != '':
        d = list(map(int, changeList['start_date'].split('-')))
        event.start_date = date(d[0], d[1], d[2])
    if changeList['start_time'] != '':
        t = list(map(int, changeList['start_time'].split(':')))
        event.start_time = time(t[0], t[1])
    if changeList['end_date'] != '':
        d = list(map(int, changeList['end_date'].split('-')))
        event.start_date = date(d[0], d[1], d[2])
    if changeList['end_time'] != '':
        t = list(map(int, changeList['end_time'].split(':')))
        event.start_time = time(t[0], t[1])
    event.save()
    return details(request, id)

def update_completed(request, id):
    event = Event.objects.get(id=id)
    event.completed = True 
    event.save()
    return index(request)
