import requests
from twilio.rest import Client

ONECALL = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = "9a32801108277bc88712428e8d2b5cd4"
ACCOUNT_SID = "AC438abcd526184fcc2c81c8dc4602c7d9"
AUTH_CODE = "114da08405b77f462116da33882ed0a8"
MY_LATITUDE = 37.548271
MY_LONGITUDE = -121.988571
parameters={
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,daily,minutely"
}

response = requests.get(ONECALL, params=parameters)
response.raise_for_status()
weather_data = response.json()
client = Client(ACCOUNT_SID, AUTH_CODE)

for hour in range(0 , 12):
    if weather_data["hourly"][hour]["weather"][0]["id"] > 700:
        message = client.messages.create(
            body = "It's going to rain today ☔️",
            from_ = "+18777646749",
            to = "5106815362"
        )
        break
