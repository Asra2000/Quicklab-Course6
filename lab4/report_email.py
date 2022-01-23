'''
Script to process supplier fruit description data from 
supplier-data/descriptions directory. 
'''

import os
import datetime
import reports
import emails

folder = "supplier-data/descriptions/"
attachment = "/tmp/processed.pdf"

def main():
    # Process the data
    date = datetime.datetime.now()
    report_title = "Processed Update on {} {}, {}".format(
        date.strftime("%d"), date.strftime("%B"), date.strftime("%Y"))
    paragraph  = {}
    for file in os.listdir(folder):
        lines = open(folder + file, 'r').read().splitlines()
        paragraph[lines[0].strip()] = lines[1].strip()
    # Generate Pdf
    reports.generate_report(attachment, report_title, paragraph)
    # Send the email
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    subject =  "Upload Completed - Online Fruit Store"
    message = emails.generate_email(attachment, sender, receiver, body, subject)
    emails.send_email(message)

if __name__ == "__main__":
    main()