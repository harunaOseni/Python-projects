import random
import pandas as pd
import smtplib
import datetime as dt

current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

email = ""
password = ""

random_index_number = random.randint(1, 3)

with open(f"Bday Email Sender/letter_templates/letter_{random_index_number}.txt") as f:
    letter = f.readlines()

with open('Bday Email Sender/birthdays.csv', 'r') as f:
    birthdays = pd.read_csv(f)

    for index, row in birthdays.iterrows():
        if current_month == row['month'] and current_day == row['day']:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(email, password)
                subject = f"Happy Birthday {row['name']}!"
                body = ''.join(letter).replace('[NAME]', row['name'])
                msg = f"Subject: {subject}\n\n{body}"
                smtp.sendmail(email, row['email'], msg)
