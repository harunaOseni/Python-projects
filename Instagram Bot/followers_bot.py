from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class FollowersBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.chrome_driver_path = r"C:\Users\oseni haruna\OneDrive\Documents\programming resources\chromedriver.exe"
        self.follower_bot = webdriver.Chrome(
            executable_path=self.chrome_driver_path)
        self.follower_bot.maximize_window()

    def login(self):
        self.follower_bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        self.user_name_field = self.follower_bot.find_element_by_name(
            "username")
        self.user_name_field.send_keys(self.username)

        time.sleep(3)
        self.password_field = self.follower_bot.find_element_by_name(
            "password")
        self.password_field.send_keys(self.password)

        time.sleep(3)

        self.password_field.send_keys(Keys.ENTER)

    def use_search_bar(self):
        time.sleep(3)
        self.search_bar = self.follower_bot.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        time.sleep(3)
        self.search_bar.send_keys("mark zuckerberg")
        time.sleep(3)
        self.search_bar.send_keys(Keys.ENTER)
        time.sleep(3)
        self.search_auto_suggestion = self.follower_bot.find_element_by_xpath(
            '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]')
        self.search_auto_suggestion.click()

    def follow_users_following(self):
        time.sleep(3)
        self.following_button = self.follower_bot.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
        self.following_button.click()
        time.sleep(3)
        self.following_card = self.follower_bot.find_elements_by_tag_name("li")
        for people in self.following_card:
            try:
                people.find_element_by_tag_name("button").click()
                time.sleep(3)
            except Exception as ex:
                print(ex)

    def keep_screen_on(self):
        time.sleep(10000)


follower_bot = FollowersBot("", "")
follower_bot.login()
follower_bot.use_search_bar()
follower_bot.follow_users_following()
follower_bot.keep_screen_on()
