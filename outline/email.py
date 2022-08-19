from .models import User, Table, Event 
import smtplib, os, ssl 

# must have two factor auth enabled 
# password is given from App Passwords -> 'myaccount.google.com/apppasswords'
# password is not email password 

PORT = 465
SMTP_SERVER = 'smtp.gmail.com'
FILE = 'email_credentials.txt'
FILE_DIR = '/User/Desktop/outlinex'

class Email: 

    def __init__(self, message):
        self.message = message 
        try: 
            file = open(os.path.join(FILE_DIR, FILE))
            self.user = file.readline() 
            self.pw = file.readline()

        except:
            print(Exception)

    def send(self):
        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context)
            server.login(self.__user, self.__password)
            server.sendmail(self.__user, self.__user, self.message)
            
        except smtplib.SMTPResponseException as exception:
            print(str(exception))


