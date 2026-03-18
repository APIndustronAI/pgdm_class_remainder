import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("OUTLOOK_EMAIL")
PASSWORD = os.getenv("OUTLOOK_PASSWORD")

def send_mail(students, subject, link, minutes):

    msg = MIMEMultipart()

    msg["From"] = str(EMAIL)
    msg["To"] = ", ".join(students)
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

    msg.attach(MIMEText(body, "plain", "utf-8"))

    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login(str(EMAIL), str(PASSWORD))

    server.sendmail(str(EMAIL), students, msg.as_string())

    server.quit()