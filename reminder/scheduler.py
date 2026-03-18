import pandas as pd
from datetime import datetime, timedelta
from email_service import send_mail
import os
from dotenv import load_dotenv

load_dotenv()

WINDOW45 = int(os.getenv("REMINDER_WINDOW_45", 12))
WINDOW10 = int(os.getenv("REMINDER_WINDOW_10", 11))

STUDENTS = [
    "arunprakashr123@gmail.com"
]

def run_scheduler():
    URL = "https://docs.google.com/spreadsheets/d/1rZm-MQ31I43vxfA561_sW2grmzNiKA20YxUmfZZDsjQ/edit?usp=drive_link"
    df = pd.read_csv(URL)

    now = datetime.utcnow() + timedelta(hours=5,minutes=30)

    for i in range(len(df)):

        class_time = datetime.strptime(str(df.loc[i,"datetime"]), "%Y-%m-%d %H:%M")

        if df.loc[i,"reminder45_sent"] == "no":
            if now >= class_time - timedelta(minutes=WINDOW45) and now < class_time - timedelta(minutes=WINDOW45-5):
                send_mail(STUDENTS, df.loc[i,"subject"], df.loc[i,"link"], WINDOW45)
                df.loc[i,"reminder45_sent"] = "yes"

        if df.loc[i,"reminder10_sent"] == "no":
            if now >= class_time - timedelta(minutes=WINDOW10) and now < class_time:
                send_mail(STUDENTS, df.loc[i,"subject"],df.loc[i,"link"], WINDOW10)
                df.loc[i,"reminder10_sent"] = "yes"

    df.to_csv("data/schedule.csv",index=False)
