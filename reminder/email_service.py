import smtplib
import os

EMAIL = os.getenv("OUTLOOK_EMAIL")
PASSWORD = os.getenv("OUTLOOK_PASSWORD")

STUDENTS = ["arunprakashr123@gmail.com"]

def send_mail(subject, minutes, link):

    server = smtplib.SMTP("smtp.office365.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)

    message = f"""Subject: PGDM Cohort3 {subject} Weekend Class Reminder
Reminder 🚨

Hi Students,

This is a reminder that our **{subject}** class starts in **{minutes}** minutes.
Join Link: {link}

Be ready before start time. Join early to avoid attendance issues.

Thanks,
AP
"""

    server.sendmail(EMAIL, STUDENTS, message)
    server.quit()
