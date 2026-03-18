import pandas as pd
import os
from datetime import datetime, timedelta
from email_service import send_mail   # ⭐ IMPORTANT IMPORT

SHEET_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ4Ku3ZAYr79s_-mMWSwCdCmWchh3VD0CEXrsVqoz2rVyT95GI-mJeQIRRRvj88Z_u87qJUXHr4dmp6/pub?output=csv"
LOG_FILE = "sent_log.txt"

def already_sent(key):
    if not os.path.exists(LOG_FILE):
        return False
    with open(LOG_FILE, "r") as f:
        return key in f.read()

def mark_sent(key):
    with open(LOG_FILE, "a") as f:
        f.write(key + "\n")

def run_scheduler():

    df = pd.read_csv(SHEET_URL)
    now = datetime.utcnow() + timedelta(hours=5, minutes=30)
    for i in range(len(df)):
        subject = df.loc[i, "subject"]
        link = df.loc[i, "link"]
        class_time = datetime.strptime(
            df.loc[i, "datetime"],
            "%Y-%m-%d %H:%M"
        )

        key30 = subject + "_30"
        key10 = subject + "_10"

        if now >= class_time - timedelta(minutes=30):
            if not already_sent(key30):
                send_mail(subject, 30, link)
                mark_sent(key45)

        if now >= class_time - timedelta(minutes=10):
            if not already_sent(key10):
                send_mail(subject, 10, link)
                mark_sent(key10)
