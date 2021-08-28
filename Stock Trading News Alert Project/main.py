from twilio.rest import Client
from decouple import config
import requests
import html
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_VANTAGE_API_KEY = config('ALPHA_VANTAGE_API_KEY')
NEWS_API_KEY = config('NEWS_API_KEY')
KEYWORD = "TSLA"
account_sid = config('TWILIO_ACCOUNT_SID')
auth_token = config('TWILIO_AUTH_TOKEN')


# STOCK PRICE
parameter = {"function": "TIME_SERIES_DAILY",
             "symbol": STOCK, "apikey": ALPHA_VANTAGE_API_KEY}

tesla_stock_price_response = requests.get(
    "https://www.alphavantage.co/query", params=parameter)

tesla_stock_price_response.raise_for_status()

tesla_stock_price_json = tesla_stock_price_response.json()

get_last_refreshed = tesla_stock_price_json["Meta Data"]["3. Last Refreshed"][0:10]
get_last_refreshed_date = get_last_refreshed.split("-")
get_day_in_month = get_last_refreshed_date[2]
get_previous_day_in_month = int(get_day_in_month[0:2]) - 1
get_previous_day_in_month = str(get_previous_day_in_month)

get_previous_date_before_refreshed_date = get_last_refreshed_date[0] + \
    "-" + get_last_refreshed_date[1] + "-" + get_previous_day_in_month

previous_day_close_price = float(
    tesla_stock_price_json["Time Series (Daily)"][get_last_refreshed]["4. close"])
day_before_previous_day_close_price = float(
    tesla_stock_price_json["Time Series (Daily)"][get_previous_date_before_refreshed_date]["4. close"])


percent_change = (previous_day_close_price -
                  day_before_previous_day_close_price) / day_before_previous_day_close_price * 100

news_parameter = {"apiKey": NEWS_API_KEY,
                  "q": KEYWORD,
                  "from": get_last_refreshed_date,
                  "sortBy": "popularity",
                  "to": get_previous_date_before_refreshed_date,
                  "language": "en"}

tesla_news_request = requests.get(
    "https://newsapi.org/v2/everything", params=news_parameter)
tesla_news_request.raise_for_status()
tesla_news_result = tesla_news_request.json()["articles"][0:3]

arrow = "🔺"

if percent_change < -5:
    arrow = "🔻"

news_01 = html.unescape(("".join([f"{STOCK}: {arrow} {percent_change:.2f}% \n", "Headline: " + tesla_news_result[0]
                                  ["title"] + " \n", "Brief: " + tesla_news_result[0]["description"]])))

news_02 = html.unescape("".join([f"{STOCK}: {arrow} {percent_change:.2f}% \n", "Headline: " + tesla_news_result[1]["title"] + " \n",
                                 "Brief: " + tesla_news_result[1]["description"]]))

news_03 = html.unescape("".join([f"{STOCK}: {arrow} {percent_change:.2f}% \n", "Headline: " + tesla_news_result[2]["title"] + " \n",
                                 "Brief: " + tesla_news_result[2]["description"]]))


# SEND SMS
# if the percent change is increased or decreased by 5%
if percent_change > 5 or percent_change < -5:
    for news in [news_01, news_02, news_03]:
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body="{}".format(news),
                            from_="+18328645184",
                            to='+18327578493'
                        )
