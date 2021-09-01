import requests
from datetime import datetime
import smtplib
response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()

iss_data = response.json()

iss_longitude = float(iss_data['iss_position']['longitude'])
iss_latitude = float(iss_data['iss_position']['latitude'])

iss_position = (iss_longitude, iss_latitude)


mylatitude = 29.760427
mylongitude = -95.369804

my_position = (mylongitude, mylatitude)


paramter = {'lat': mylatitude, 'lng': mylongitude, "formatted": 0}

response = requests.get('https://api.sunrise-sunset.org/json', params=paramter)
response.raise_for_status()

data = response.json()

sunrise_data = int(data['results']['sunrise'].split('T')[1].split(":")[0])
sunset_data = int(data['results']['sunset'].split('T')[1].split(":")[0])


current_time = datetime.now()
todays_hour = current_time.hour

mynew_position = (mylongitude-5, mylatitude+5)


if ((iss_position[0] >= mynew_position[0] and iss_position[0] <= my_position[0]) and (iss_position[1] >= mynew_position[1] and iss_position[1] <= my_position[1])) and (todays_hour >= sunrise_data or todays_hour <= sunset_data):
    with smtplib.SMTP_SSL('smtp.gmail.com', 578) as connection:
        connection.login('', '')
        connection.starttls()
        subject = 'Alert'
        body = 'The ISS is over you!'
        email_text = f'Subject: {subject}\n\n{body}'
        connection.sendmail(from_addr="",
                            to_addr="", msg=f"Subject: {subject}\n\n{body}")
