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

