import math

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


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

#NewsApi = 9d83f092155346cc9d7fae3522f7bd6e
#Alpha Vantage = 9679K84YY8OMVBBS
#Twillo SID = AC05f0ea84be4dd923f1a3cdc81d27a531
#Twilo Auth = 198642796b54075617d5a75a91492ffe

# import requests
#
# url = ('https://newsapi.org/v2/everything?'
#        'q=Apple&'
#        'from=2023-07-01&'
#        'sortBy=popularity&'
#        'apiKey=9d83f092155346cc9d7fae3522f7bd6e')
#
# response = requests.get(url)
#
# print(response.json())

import requests
from twilio.rest import Client

def get_articles(day):
    url = ('https://newsapi.org/v2/everything?'
           f'q={STOCK}&'
           f'from={day}&'
           'sortBy=popularity&'
           'apiKey=9d83f092155346cc9d7fae3522f7bd6e')

    response = requests.get(url)

    first_title = response.json()['articles'][0]['title']
    first_description = response.json()['articles'][0]['description']

    second_title = response.json()['articles'][1]['title']
    second_description = response.json()['articles'][1]['description']

    return {first_title: first_description, second_title: second_description}


def send_sms(perc=5, **kwargs):
    account_sid = 'AC05f0ea84be4dd923f1a3cdc81d27a531'
    auth_token = '198642796b54075617d5a75a91492ffe'
    client = Client(account_sid, auth_token)

    for key, value in kwargs.items():
        message = client.messages.create(
            from_='+18145262067',
            body=f'{perc}\n{key}\n\n{value}',
            to='+48737365338'
        )
        print(message.sid)

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey=9679K84YY8OMVBBS'
r = requests.get(url)
data = r.json()
data2 = data['Time Series (Daily)']
iter_data = iter(data2)

print(data['Time Series (Daily)'])
#print(data2[next(iter_data)]['1. close'])

previous_close = 0.0
for day in data2:
    close = float(data2[day]["4. close"])
    if previous_close == 0:
        previous_close = close
    else:
        percent = (previous_close - close) / ((previous_close + close) / 2) * 100
        previous_close = close
        if math.fabs(percent) > 5:
            print(f'Day: {day}, spike of: {round(percent,2)}%')
            articles = get_articles(day)
            send_sms(percent = percent, **articles)
            break




