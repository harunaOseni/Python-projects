# Twitter internet speed complaining bot.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# CONSTANT
PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = r"C:\Users\oseni haruna\OneDrive\Documents\programming resources\chromedriver.exe"
TWITTER_USERNAME = "ArmstrongChesky"
TWITTER_PASSWORD = "Oseni6716"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")
        time.sleep(6)
        self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(65)
        self.internet_speed_down = self.driver.find_element_by_css_selector(
            '#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.result-area.result-area-test > div > div > div.result-container-speed.result-container-speed-active > div.result-container-data > div.result-item-container.result-item-container-align-center > div > div.result-data.u-align-left > span')
        self.internet_speed_up = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        print("Internet speed down: " + str(self.internet_speed_down))
        print("Internet speed up: " + str(self.internet_speed_up))

    def tweet_at_provider(self):
        time.sleep(10)
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        self.username = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        self.username.send_keys(TWITTER_USERNAME)
        self.password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        self.password.send_keys(TWITTER_PASSWORD)
        self.password.send_keys(Keys.ENTER)
        time.sleep(10)
        tweet_box = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(
            f"Hey Internet Service Provider! My internet speed is {self.down} down and {self.up} up. I'm sorry for the inconvenience. I'm a bot. Please don't reply to this message.")
        time.sleep(10)
        tweet_send_button = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_send_button.click()
        time.sleep(5)

    def do_not_close(self):
        time.sleep(10000)


speed_bot = InternetSpeedTwitterBot()

speed_bot.get_internet_speed()
speed_bot.tweet_at_provider()
speed_bot.do_not_close()
