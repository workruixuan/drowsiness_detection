from email.message import EmailMessage
from dotenv import load_dotenv
import os
import smtplib
import re 

from googlesheetsMgr import Googlesheets

class EmailMgr:
    gg = Googlesheets()
    receiverEmail = gg.getEmail("Rui Xuan")


    #check valid of email
    def checkEmailValid(s):
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat,s):
            return True
        return False
    
    if receiverEmail != 0 & checkEmailValid(receiverEmail) == True:
        # load env variables
        load_dotenv() 
        msg = EmailMessage()
        msg['Subject'] = 'Subject test'
        msg['From'] = os.getenv("EMAIL_ADDRESS")
        msg['To'] = receiverEmail
        msg.set_content('how about content')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login(os.getenv("EMAIL_ADDRESS"),os.getenv("EMAIL_PASSWORD"))
            print('done')
            smtp.send_message(msg)
    else:
        print("Invalid!")
    

