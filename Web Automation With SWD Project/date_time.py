from selenium import webdriver
import time

chrome_driver_path = r"C:\Users\oseni haruna\OneDrive\Documents\programming resources\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# open a web page
driver.get("https://www.python.org/")

time_of_event = driver.find_elements_by_css_selector(".shrubbery time")[5:10]

event_name = driver.find_elements_by_css_selector(".shrubbery a")[7:12]

time_event_dict = {
    key: {time_of_event[key].text: event_name[key].text}
    for key in range(5)
}

print(time_event_dict)
