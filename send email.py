import smtplib
import os
from email.message import EmailMessage
import imghdr  # Library to determine the type of image

# Fetching email credentials from environment variables
email_id = os.environ.get('EMAIL_ADDR')
email_pass = os.environ.get("EMAIL_PASS")

# Establishing connection with SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_id, email_pass)
    
    # Composing the email
    subject = 'Fight against Coronavirus'
    body = "Hey, hi let's fight against Coronavirus by staying at home"
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_id
    msg['To'] = 'sputnik6329@gmail.com'
    msg.set_content(body)
    
    # Adding attachments
    files = ['modi.jpg', 'modi1.jpg', 'modi2.jpg']
    for file in files:
        with open(file, 'rb') as f:  # Opening file in binary mode
            file_data = f.read()
            file_type = imghdr.what(f.name)  # Determining the type of image
            file_name = f.name
            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    
    # Sending the email
    smtp.send_message(msg)