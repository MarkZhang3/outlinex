from datetime import datetime
from outline.models import User, Table, Event 
from apscheduler.schedulers.background import BackgroundScheduler # apscheduler package
from . import email

#vqoaywnbfhcjgshb

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(email.job, 'interval', minutes=30)
    scheduler.start()