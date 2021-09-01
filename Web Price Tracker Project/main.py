from twilio.rest import Client
from decouple import config
from bs4 import BeautifulSoup
import requests as req
import lxml


product_url = "https://www.ebay.com/itm/233996853637?_trkparms=ispr%3D1&hash=item367b4ca185:g:TJIAAOSwtn1gkmgc&amdata=enc%3AAQAGAAACkPYe5NmHp%252B2JMhMi7yxGiTJkPrKr5t53CooMSQt2orsSRAQR8FABHjfpFoyRlXhWmaW4DEBbnF7JbRPuA78XrS%252F5Xd5Qo9dIHnfajEhSR7T5%252BTpQn53lXl2heJzt2xWvtOhYa3nOo%252BpjPO9d9kpNqYKNA3wXxiIAtaWqboRNCKNfxBwzC%252BtRxSsM5QMiYL2NFiJalKj2X7FrzgfjZrqzyipjYQmOJE4h8A%252FjHk7JbGROKnRvpnJx12Z61n1z63qiOADZAzG%252FzwgdRoXziNDtttjvQ3BIaAF5NnNpJ5T%252B8JPUhn4KZwpYbT5PWMlM%252BJexGdP9xba690VBEbt4YFMknMMlOoxq8I2ot3NZMMxpzYDVR7uFuGJ5PoSBlPtoQAgXL8yAY5p7KCf2uKaBlEcO7fURbYM5Rgu0VcA7nWWM%252BpXw92vj%252BrYSQ87y5mKD1I320TZR%252Bu8HD0zF%252BHAbm%252BK%252BrCF77S4qqtFJg6OCOqzFXE%252BwO5tYxHHLk2QUm%252BW85b93APm03lFLQNFTpUWKK3NwnFbEXtDdAd6WNTPC7MgpRfF8uD9%252BpMP4yXtlN6wm4Uh%252F3qH%252FV4%252B9XgKI4tDQwcqdUcRDBHMl0vF%252F23jkvZumYsw%252BfV15tDadVfDVjMcICoBpZbXiEfzY6SHx6QWH6N2B8bjDodhmADzBKCpRFCfvzb9dOW8uoZB4l5AzhunIUfG0KaUSJIqWOJjqBIsOEfncSEdUvqGnnxwCbWXTeACUN%252B4duuk5jxP58CFn%252F74Zke5jXl1xICQ%252BXmlHPwmhsRP2umGypNiKfxBfppWv8tAKZcgI8bw8P5ZPasiuvqxTgaCiTseSH9LQ4YdfwXRk2%252ByNWdgZyv6ew61EZTAtUDBZLYrK%7Campid%3APL_CLK%7Cclp%3A2334524"


account_sid = config('ACCOUNT_SID')
auth_token = config('AUTH_TOKEN') 
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}

webpage = req.get(product_url, headers=headers)

soup = BeautifulSoup(webpage.content, features="lxml")

# prcIsum

price_of_product = soup.find("span", {"id": "prcIsum"})
price = float(price_of_product.text[4:9])


# check if price becomes lower than the current price
if price == 32.49:
    print("Price of product has gone down")
    # send email
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Hurray! The price of the smart glasses you want to purchase is below the normal price!",
        from_='',
        to=''
    )
    print(message.status)
