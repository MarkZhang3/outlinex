from django.shortcuts import render, redirect
from datetime import datetime, date, time
from .models import Table, Event, AppPassword 
from .forms import RegisterForm, PasswordForm
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/outline/login')
def index(request):
    user = request.user.username
    userTables = [t for t in Table.objects.all() if t.user == user]
    content = {
        'tables': userTables,
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
        t = Table(name=table_name, user = request.user)
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

def delete_table(request, id):
    table = Table.objects.get(id=id)
    table.delete()
    return index(request)

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = RegisterForm()
    content = {
        'form': form,
    }
    return render(request, 'sign_up.html', content)

def app_password(request):
    return render(request, 'app_password.html')

def add_app_password(request):
    user = request.user 
    password = request.POST['app_password']
    pw = AppPassword.objects.create(user=user, app_password=password)
    pw.save()
    return redirect('index')

def logout_view(request):
    logout(request)
    return redirect('login')
