# Tinder Swiping bot
from selenium import webdriver
import time as t

chrome_driver = r"C:\Users\oseni haruna\OneDrive\Documents\programming resources\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)

driver.maximize_window()

driver.get("https://tinder.com/")

# storing the current window handle to get back to dashbord
main_page = driver.current_window_handle

log_in_button = driver.find_element_by_xpath(
    '//*[@id="q-2020625691"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_button.click()


t.sleep(5)

google_button = driver.find_element_by_xpath(
    '//*[@id="q545960529"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
google_button.click()


t.sleep(10)  # wait for google to load


# changing the handles to access login page
for handle in driver.window_handles:
    if handle != main_page:
        login_page = handle  # getting the handle of the login page

# change the control to signin page
driver.switch_to.window(login_page)

email_field = driver.find_element_by_tag_name("input")

# type email in the email field
email_field.send_keys("")
# click enter
email_field.send_keys(u'\ue007')

t.sleep(5)


password_field = driver.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
t.sleep(3)

# enter password
password_field.send_keys("")
# click enter
password_field.send_keys(u'\ue007')

t.sleep(5)

# switch to the dashbord
driver.switch_to.window(main_page)

t.sleep(5)

# click on allow location
location_button = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div/div/div[3]/button[1]')

location_button.click()

t.sleep(10)

# click on not_interested button
not_interested_button = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')
not_interested_button.click()
t.sleep(5)

# accept cookies
cookies_button = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[2]/div/div/div[1]/button')
cookies_button.click()

# keep swiping left
while True:
    t.sleep(10)
    swipe_left_button = driver.find_element_by_css_selector(
        '#q-2020625691 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-pink\) > button > span > span')
    swipe_left_button.click()


t.sleep(10000)
