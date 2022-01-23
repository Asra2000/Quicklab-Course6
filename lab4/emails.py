'''
Script to email the PDf created.
'''
import smtplib
import os
from email.message import EmailMessage
import mimetypes


def generate_email(attachment, sender, receiver, body, subject):
    message = EmailMessage()
    
    message['From'] = sender
    message['To'] = receiver
    message['Body'] = body
    message['Subject'] =subject
    if attachment != None:
        mime_type, _ = mimetypes.guess_type(attachment)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment, 'rb') as ap:
            message.add_attachment(ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=os.path.basename(attachment))

    return message

def send_email(message):
    """Sends the email package to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()