from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time as timeForSleep

# selenium webdriver
chrome_driver = r"C:\Users\oseni haruna\OneDrive\Documents\programming resources\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

# request headers
# what is a request header? a header is a piece of information that tells the server what type of information you are sending to it.
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

# CONSTANTS
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
zillow_listing = requests.get(url=URL, headers=req_headers)

# make soup
soup = BeautifulSoup(zillow_listing.text, 'html.parser')

# scrape prices from zillow
zillows_listing_prices = soup.find_all(class_='list-card-price')


# scrape addresses from zillow
zillows_listing_addresses = soup.find_all(class_='list-card-addr')

# scrape links from zillow
zillows_listing_links = soup.find_all(class_='list-card-link')

# Create a list of links for all the listings you scraped. e.g.
list_for_links = [link.get("href") for link in zillows_listing_links]

# Create a list of prices for all the listings you scraped. e.g.
list_for_prices = [price.get_text() for price in zillows_listing_prices]
list_for_prices = [price[:6] for price in list_for_prices]


# Create a list of addresses for all the listings you scraped. e.g.
list_for_addresses = [address.get_text()
                      for address in zillows_listing_addresses]

# selenium web driver program
driver_url = "https://docs.google.com/forms/d/e/1FAIpQLSfugS9YZlUWZI30koBl8xAXVSbJgDF4u2aLgmxJabKuzVsULw/viewform"

driver.maximize_window()
driver.get(driver_url)

# fill out the form
timeForSleep.sleep(5)

# loop through the three list
for i in range(len(list_for_prices)):
    # fill out the form
    timeForSleep.sleep(5)
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(list_for_addresses[i])
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(list_for_prices[i])
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(list_for_links[i])
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span').click()
    timeForSleep.sleep(10)
    if i < len(list_for_prices)-1:
        driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


# keep window open
timeForSleep.sleep(1000)
