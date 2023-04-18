import requests
import datetime as dt
import os
from twilio.rest import Client

API_CODE="IW8ONT9PL7TG27MP"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
today=dt.datetime.today()
NEW_API_KEY="381db326afb14ee3b9925b30854d9912"
TWILIO_SID="AC6cfd6dd68cf837a8718c837471652a68"
TWILIO_TOKEN="3959e6a724d5ee96650244c207a19d46"

parameters={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":API_CODE
}

response=requests.get(url="https://www.alphavantage.co/query",params=parameters)
data=response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items()]
yesturday_data=data_list[0]
yesturday_closing_price=yesturday_data["4. close"]

day_before_yesturday=data_list[1]
day_before_closing_price=day_before_yesturday["4. close"]
diffrance=abs(float(yesturday_closing_price)-float(day_before_closing_price))
diff_precent=(diffrance/float(yesturday_closing_price))*100

if diff_precent>5:
    news_params={
        "apiKey":NEW_API_KEY,
        "qInTitle":COMPANY_NAME
    }
    news_response=requests.get(url="https://newsapi.org/v2/everything",params=news_params)
    articles=news_response.json()["articles"]
    three_articles=articles[:3]
    articels_format=[f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client=Client(TWILIO_SID,TWILIO_TOKEN)
    for article in articels_format:
        message = client.messages.create(
            body=article,
            from_='+15076195218',
            to='+972509988726'
        )

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

