#!/usr/bin/python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
server = smtplib.SMTP(host='<your-smtp-server>',port=25)

# create message object instance
msg = MIMEMultipart()
message = "Thank you"
# setup the parameters of the message
msg['From'] = "<sender-email>"
msg['To'] = "<receiver-email>"
msg['Subject'] = "Test email"
# add in the message body
msg.attach(MIMEText(message, 'plain'))
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
