import requests
from twilio.rest import Client
from decouple import config
# An environment variable is a variable whose value is set outside of a program.
# The value of the environment variable is available to the entire program.

LONG: float
LAT: float

LAT = 29.760427
LONG = -95.369804
API_KEY = config('API_KEY')
account_sid = config('ACCOUNT_SID')
auth_token = config('AUTH_TOKEN')


parameter = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY
} 


weather_response = requests.get(
    "https://api.openweathermap.org/data/2.5/onecall", params=parameter)
weather_response.raise_for_status()
weather_data_json = weather_response.json()
rain_data = []
# weather_data_json["hourly"][1]["weather"][0]["id"]
for _ in range(0, 12):
    rain_data.append(weather_data_json["hourly"][_]["weather"][0]["id"])

print(rain_data)

will_rain = False

for data in rain_data:
    if data < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Dude, it's Gideon your personal robot, take an umbrella, It's gonna rain today😢😪!",
        from_='+18328645184',
        to='+18327578493'
    )
    print(message.status)
