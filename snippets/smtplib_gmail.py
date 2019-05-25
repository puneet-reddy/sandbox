#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

sender = 'email of the sander'
recepient = 'email of the recepient'

msg = MIMEMultipart()

# Construct the message
message = 'This is a test message sent via gmail using smtplib in python'
msg['From'] = sender
msg['To'] = recepient
msg['Subject'] = 'Test mail'
msg.attach(MIMEText(message, 'plain'))

# If you want to add an attachment
with open('path to file', 'rb') as attachment:
    base = MIMEBase('application', 'octet-stream')
    base.set_payload(attachment.read())
    encoders.encode_base64(base)
    base.add_header('Content-Disposition',
                    'attachment; filename=filename with extension')
    msg.attach(base)


mailer = smtplib.SMTP('smtp.gmail.com', 587)

# Secure it with TLS
mailer.starttls()
mailer.login(sender, 'my_password')
mailer.sendmail(sender, recepient, msg.as_string())

# Terminate the session
mailer.quit()
