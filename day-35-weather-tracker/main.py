import requests
import os
from dotenv import load_dotenv
# import pandas
from twilio.rest import Client

load_dotenv() # loads all the env vars into the present file


api_key = os.getenv("OWM_API_KEY")

my_lat =21.166100
my_lng = 75.857803



account_sid ="AC9486b84fca36884c463626c6e16fcc22"

auth_token = os.getenv("TWILIO_AUTH_TOKEN")
website_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
parameters ={
    "lat": my_lat,
    "lon": my_lng,
    "appid": api_key,
    "cnt" : 4,
}


# NOTE : requests.get() requires a full URL, including the protocol. including https://
data = requests.get(url = website_endpoint , params=parameters)
print(data.raise_for_status())
response = data.json()["list"]
weather_details = []
temp={}
for entry in response:
    temp["At"]= entry["dt_txt"]
    temp["weather"]=entry["weather"][0]["description"]
    weather_details.append(temp)
    temp={}


msg = (f"Daily Forecast :\n")
for unit in weather_details:
    msg += f"At {unit["At"]}, the weather description is:- {unit["weather"]}\n"

client = Client(account_sid , auth_token)
message = client.messages.create(
    body=msg,
    from_="+17152009645",
    to="+917887979181",
)

# report = []
# di ={}
# for entry in response:
#     di["id"] = entry["weather"][0]["id"]
#     di["description"] = entry["weather"][0]["description"]
#     if di not in report:
#         report.append(di)
#     di={}



# df = pandas.DataFrame(report)
#
# print(response)
# print(report)
# print(df)
