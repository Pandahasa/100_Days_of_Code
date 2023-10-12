import datetime
import smtplib
import requests
MY_LATITUDE = 37.548271
MY_LONGITUDE = -121.988571
parameters={
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json" , params=parameters)
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data = iss_response.json()
iss_lat = float(iss_data["iss_position"]["latitude"])
iss_long = float(iss_data["iss_position"]["longitude"])
time = datetime.datetime.now().hour

my_email = "sidpanda65@gmail.com"
password = "ztmzwivcwobmtfyf"

if MY_LATITUDE - 5 < iss_lat < MY_LATITUDE + 5 and MY_LONGITUDE - 5 < iss_long < MY_LONGITUDE + 5:
    if time < sunrise or time > sunset:
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="sidpanda65@outlook.com", msg="Look up, ISS visible")
        connection.close()