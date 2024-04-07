import smtplib, csv, random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Zoho Mail SMTP server details
smtp_server = 'smtp.zoho.com'
port = 587  # or 465 for SSL
username = 'getit32'
password = 'qaz1wsx2.'

# Email details
sender_email = 'getit32@zohomail.com'
receiver_email = 'renuelroberts01@gmail.com'
subject = 'Test Email'
body = 'This is a test email sent using Python and Zoho Mail.'

# Create message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Connect to the server
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Secure the connection
    server.login(username, password)
    server.send_message(message)

print('Email sent successfully!')
