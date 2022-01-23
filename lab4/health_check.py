'''
Script that will run in the background monitoring some of your system statistics: 
CPU usage, disk space, available memory and name resolution. 
Moreover, this Python script should send an email if there are problems, such as:

Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
'''
#!/usr/bin/env python3
import psutil
import os
import emails
import socket

def check_cpu_usage(sender, receiver, body):
    if psutil.cpu_percent(1) > 80:
        subject = "Error - CPU usage is over 80%"
        message = emails.generate_email(None, sender, receiver, body, subject)
        emails.send_email(message)

def check_memory_usage(sender, receiver, body):
    available = psutil.virtual_memory().available
    if  available/(1024*1024) < 500:
        subject = "Error - Available memory is less than 500MB"
        message = emails.generate_email(None, sender, receiver, body, subject)
        emails.send_email(message)

def check_disk_space(sender, receiver, body):
    disk_usage = psutil.disk_usage('/')
    disk_total = disk_usage.total
    disk_free = disk_usage.free
    threshold = disk_free / disk_total * 100
    if threshold < 20:
        subject = "Error - Available disk space is less than 20%"
        message = emails.generate_email(None, sender, receiver, body, subject)
        emails.send_email(message)

def check_hostname(sender, receiver, body):
    local_host_ip = socket.gethostbyname('localhost')
    if local_host_ip != '127.0.0.1':
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        message = emails.generate_email(None, sender, receiver, body, subject)

def main():
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    check_cpu_usage(sender, receiver, body)
    check_memory_usage(sender, receiver, body)
    check_disk_space(sender, receiver, body)
    check_hostname(sender, receiver, body)


main()