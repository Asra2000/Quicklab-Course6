'''
A script reports.py to generate PDF report to supplier
'''

#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):
    report = SimpleDocTemplate(attachment)
    styles = getSampleStyleSheet()
    report_title = Paragraph(title, styles["h1"])
    pdf = ""
    for name, weight in paragraph.items():
        pdf += "name: "+    name+"<br/>"+"weight: "+weight + '<br/><br/>'
    report.build([report_title, Spacer(1,20) ,Paragraph(pdf, styles['BodyText']), Spacer(1,20)])
    
    
