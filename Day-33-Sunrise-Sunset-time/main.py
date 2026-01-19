import requests
from datetime import datetime
import smtplib
import time

API ="https://api.sunrise-sunset.org/json"
API_ISS = "http://api.open-notify.org/iss-now.json"
MY_EMAIL = "ksp29mar04@gmail.com"
MY_PASS = "htuu sfew knfo bxcs"

MY_LAT =19.569500
MY_LNG =74.211899

def is_over_head():
    iss_pos = requests.get(url=API_ISS)
    iss_data = iss_pos.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    if abs(iss_lat - MY_LAT) <= 5 and abs(iss_lng - MY_LNG) <= 5:
        return True
    else:
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    response = requests.get(url=API, params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    sunrise_hr = int(sunrise.split("T")[1].split(":")[0])
    sunset_hr = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now()
    now_hr = time_now.hour

    if (now_hr > sunrise_hr) and (now_hr < sunset_hr):
        return False
    else:
        return True


while True:
    time.sleep(60)
    if is_night() and is_over_head():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="patilks322@gmail.com",
                                msg="Subject:ISS Tracker\n\nLook up , The ISS is over your head")
        time.sleep(600)




