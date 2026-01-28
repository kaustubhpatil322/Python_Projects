import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ACCOUNT_SID="AC9486b84fca36884c463626c6e16fcc22"
load_dotenv()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key = os.getenv("STOCK_API_KEY")

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 


parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":api_key,
}
stock_data = requests.get(url = STOCK_ENDPOINT , params=parameters)
stock_data.raise_for_status()
response = stock_data.json()
print(response)

# day_before_yesterday_date = response["Meta Data"][]

time_series = response["Time Series (Daily)"]
#to fetch first two dates
prev_dates = list(time_series.keys())

yestrday_date= prev_dates[0]
before_yesterday = prev_dates[1]
price_yesterday = float(time_series[yestrday_date]["4. close"])
price_before_yesterday = float(time_series[before_yesterday]["4. close"])
price_diff = abs(price_yesterday - price_before_yesterday)
price_diff_percent = (price_diff/price_before_yesterday)*100
print(f"{price_diff_percent}")
# sum=0
# for i in range(10):
#     yestrday_date= prev_dates[0]
#     before_yesterday = prev_dates[1]
#     price_yesterday = float(time_series[yestrday_date]["4. close"])
#     price_before_yesterday = float(time_series[before_yesterday]["4. close"])
#     price_diff = abs(price_yesterday - price_before_yesterday)
#     price_diff_percent = (price_diff/price_before_yesterday)*100
#     prev_dates = prev_dates[2:]
#     # print(price_diff)
#     sum+= price_diff_percent
#     print(price_diff_percent)
# print(f"\n{(sum/15)}")


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

news_api_key = os.getenv("NEWS_API_KEY")

if price_diff_percent>0.5:
    parameters = {
        "apiKey":news_api_key,
        "q":STOCK
    }
    news_data = requests.get(url=NEWS_ENDPOINT , params=parameters)
    news_data.raise_for_status()
    news_response = news_data.json()
    news_articles = news_response["articles"][:2]
    news_content = [
        {
            "Description": entry["description"]
        }
        for entry in news_articles
    ]

    print(news_articles)
    print(news_content)
    msg="STOCK MOVEMEMENT NOTICED!!!\n"

    for i in range(len(news_content)):
        msg+= f"News{i+1}:{news_content[i]["Description"]}\n"
        # msg+=f"Description:{news_content[i]["Description"]}\n"
    print(len(msg))
    print(msg)
    auth_token = os.getenv("AUTH_TOKEN")
    client=Client(ACCOUNT_SID , auth_token)
    message = client.messages.create(
        # messaging_service_sid='MGc9224e5c049cfaedb8b6e55bdb1c138c',
        body=msg,
        from_="+17152009645",
        to="+917887979181"
    )
    print(message.sid)




## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

