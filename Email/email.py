from outline.models import User, Table, Event 
import smtplib, os, ssl 

# must have two factor auth enabled 
# password is given from App Passwords -> 'myaccount.google.com/apppasswords'
# password is not email password 

PORT = 465
SMTP_SERVER = 'smtp.gmail.com'

class Email: 

    def __init__(self, message, pw):
        self.message = message 
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
            server.login(self.user, self.pw)
            server.sendmail(self.user, self.user, self.message)
            
        except smtplib.SMTPResponseException as exception:
            print(str(exception))


