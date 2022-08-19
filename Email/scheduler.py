from datetime import datetime
from outline.models import User, Table, Event 
from apscheduler.schedulers.background import BackgroundScheduler # using apscheduler 
from .email import Email

def job():
    events = Event.objects.filter(start_date=datetime.today())
    
#vqoaywnbfhcjgshb

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job()