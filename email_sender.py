import sys
import os
import smtplib
from email.message import EmailMessage

msg = None
content = sys.stdin.read()
if content:
    msg = EmailMessage()
    msg.set_content(content)
else:
    print("No content")
    sys.exit()

reciever = os.environ['RECIEVER']
gmail_user = os.environ['GMAIL_USER']
gmail_pass = os.environ['GMAIL_PASS']

msg['Subject'] = 'Footy Matches of Interest'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(gmail_user, gmail_pass)
server.send_message(msg, from_addr=gmail_user, to_addrs=[reciever])
server.close()
print("sent")
