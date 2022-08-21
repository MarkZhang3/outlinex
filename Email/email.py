from outline.models import User, Table, Event 
from datetime import datetime
import smtplib, os, ssl 

# must have two factor auth enabled 
# password is given from App Passwords -> 'myaccount.google.com/apppasswords'
# password is not email password 

PORT = 465
SMTP_SERVER = 'smtp.gmail.com'

class Email: 

    def __init__(self, pw):
        self.user = pw.user
        try: 
            self.username = self.user.username
            self.password = pw.app_password

        except:
            print(Exception)

    def send(self):
        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context)
            server.login(self.user.email, self.pw)
            server.sendmail(self.user.email, self.user.email, self.message)
            
        except smtplib.SMTPResponseException as exception:
            print(str(exception))

def job():
    # get all tables and user from table
    # get events from table 
    # search for user and matching app password 
    # send email 
    dateToday = datetime.today().strftime('%Y-%m-%d')
    tables = Table.objects.all()
    for table in tables:
        user = User.objects.get(username=table.user)
        for event in table.event_set.all():
            if event.completed == False and event.start_date == dateToday:
                email = Email(event.text, user.apppassword.app_password)
                email.send() 


