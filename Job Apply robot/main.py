from selenium import webdriver
import time as t
from decouple import config

chrome_driver = r"C:\Users\oseni haruna\OneDrive\Documents\programming resources\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

job_url = "https://www.linkedin.com/jobs/search/?keywords=Software+Engineer&location=San+Francisco+Bay+Area&geoId=90000084&trk=public_jobs_jobs-search-bar_search-submit"


# credentials
password = config('PASSWORD')

# log in to linked in
driver.get(job_url)

# maximize the window
driver.maximize_window()

sign_in_button = driver.find_element_by_xpath(
    '/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

username_search = driver.find_element_by_id('username')
password_search = driver.find_element_by_id('password')

# enter username and password
username_search.send_keys("harunaoseni23@gmail.com")
password_search.send_keys(password)

# click enter key
password_search.send_keys(u'\ue007')

# turn on easy apply button
easy_apply = driver.find_element_by_xpath(
    '/html/body/div[5]/div[3]/div[3]/section/div/div/div/ul/li[8]/div/button')
easy_apply.click()

t.sleep(5)

# click apply button
apply_button = driver.find_element_by_css_selector(".jobs-apply-button")
apply_button.click()

t.sleep(10)

# <button aria-label="Submit application" id="ember1143" class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view" data-control-name="submit_unify" type="button"><!---->
# <span class="artdeco-button__text">
#     Submit application
# </span></button>

# click next button
next_button = driver.find_elements_by_tag_name("button")
for button in next_button:
    if button.get_attribute("aria-label") == "Submit application":
        button.click()
        break


t.sleep(10000)
