import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("OUTLOOK_EMAIL")
PASSWORD = os.getenv("OUTLOOK_PASSWORD")

STUDENTS = [
    "arunprakashr123@gmail.com"
]

def send_mail(subject, minutes, link):

    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)

    msg["Subject"] = f"PGDM Cohort3 Reminder: {subject} Weekend Class"

    body = f"""
Reminder 🚨

Hi Students,

This is a reminder that our **{subject}** class starts in **{minutes}** minutes.

Join Link: {link}

Be ready before start time. Join early to avoid attendance issues.

Thanks,
AP
"""
    message = msg["Subject"]
    server.sendmail(EMAIL, STUDENTS, message)
    server.quit()
