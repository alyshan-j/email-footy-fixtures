import sys
import os
import smtplib
from email.message import EmailMessage

content = sys.stdin.read()

if content:
    msg = EmailMessage()
    msg.set_content(content)
else:
    print("No content")
    sys.exit()

msg['Subject'] = 'The contents' 
msg['From'] = ""
msg['To'] = os.environ['RECIEVER']

gmail_user = os.environ['GMAIL_USER']
gmail_pass = os.environ['GMAIL_PASS']

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(gmail_user, gmail_pass)
    server.send_message(msg)
    server.close()
    print("sent")
except Exception as e:
    print(e)
