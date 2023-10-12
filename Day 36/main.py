import requests
from twilio.rest import Client
from datetime import *
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "7CWG6ENFC1BY40KW"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "86e7c942ab33437d9d217bacdba35cbf"

ACCOUNT_SID = "AC438abcd526184fcc2c81c8dc4602c7d9"
AUTH_CODE = "114da08405b77f462116da33882ed0a8"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": STOCK_API_KEY,
}
news_parameters = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME
}
stock_response = requests.get(STOCK_ENDPOINT, params= stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]

news_response = requests.get(NEWS_ENDPOINT, params = news_parameters)
three_articles = news_response.json()["articles"][:3]

def date_getter(days_ago):
    while (date.today() - timedelta(days_ago)).weekday() >= 5:
        days_ago += 1
    return str(date.today() - timedelta(days_ago))
    
client = Client(ACCOUNT_SID, AUTH_CODE)



#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
yesterday_closing = float(stock_data[date_getter(1)]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing = float(stock_data[date_getter(2)]["4. close"])

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
day_difference = abs(yesterday_closing - day_before_yesterday_closing)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = round(100*(day_difference / yesterday_closing))

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
articles = [f"Headline: {article['title']} \n Brief: {article['description']}" for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio. 
print(f"TSLA: {percentage_difference} \n {articles}")
for article in articles:
    if yesterday_closing < day_before_yesterday_closing:
        message = client.messages.create(
            body = f"TSLA: 🔻{percentage_difference} \n {article}",
            from_ = "+18777646749",
            to = "5106815362",
            )   
    else:
        message = client.messages.create(
        body = f"TSLA: 🔺{percentage_difference} \n {article}",
        from_ = "+18777646749",
        to = "5106815362",
        )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

