from selenium import webdriver
# import time

chrome_driver = r"C:\Users\oseni haruna\OneDrive\Documents\programming resources\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name_search = driver.find_element_by_name("fName")
first_name_search.send_keys("Haruna")
last_name_search = driver.find_element_by_name("lName")
last_name_search.send_keys("Oseni")
email_search = driver.find_element_by_name("email")
email_search.send_keys("harunaoseni23@gmail.com")

button = driver.find_element_by_xpath('/html/body/form/button')
button.click()


# time.sleep(10000)