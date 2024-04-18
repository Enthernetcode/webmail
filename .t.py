import smtplib, csv, random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Zoho Mail SMTP server details
'''with open("mails.csv", "r") as file:
                reader = csv.reader(file)
                rows = list(reader)
                rows = rows[1:]
            if rows:
                with open("mails.csv", "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(rows)
'''
smtp_server = 'smtp.zoho.com'
port = 587  # or 465 for SSL
username = 'getit32'
password = 'qaz1wsx2.'
with open('emails/message1.txt', 'r') as l:
 msg = l.read()
with open('mails.csv', 'r') as mail:
 k = csv.reader(mail)
 l = list(k)
 for i in l:
   p= i
   print(p)
# Email details
   sender_email = 'getit32@zohomail.com'
   receiver_email = p #['renuelroberts01@gmail.com','enthernetcode@gmail.com','renuelroberts0@gmail.com','renuelroberts02@gmail.com']
   subject = 'Test Email'
   body = msg #'This is a test email sent using Python and Zoho Mail.'

   for receiver in receiver_email:
     print (receiver) # Create message
     message = MIMEMultipart()
     message['From'] = sender_email
     message['To'] = receiver
     message['Subject'] = subject
     message.attach(MIMEText(body, 'plain'))
     print (receiver)
# Connect to the server
   with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Secure the connection
    server.login(username, password)
    server.send_message(message)

   print('Email sent successfully!')
