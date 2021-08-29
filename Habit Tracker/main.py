import requests
from datetime import datetime

# constants
USERNAME = "harunaoseni"
TOKEN = "ireallyenjoyprogramming"
URL = "https://pixe.la/v1/users"
ID = "hackathonid"

# creating a user account
user_data = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

url = URL

user_create_account_response = requests.post(url=url, json=user_data)

# create a graph

graph_url = "https://pixe.la/v1/users/{}/graphs".format(USERNAME)

API_HEADER = {
    "X-USER-TOKEN": TOKEN,
}

graph_data = {
    "id": "hackathonid",
    "name": "All Night Hackathons",
    "unit": "commit",
    "type": "int",
    "color": "momiji",
    "timezone": "US/Central",
}

create_graph_response = requests.post(
    url=graph_url, json=graph_data, headers=API_HEADER)

# post a value to the graph

today = datetime.today().strftime("%Y%m%d")

post_to_graph_url = "https://pixe.la/v1/users/{}/graphs/{}".format(
    USERNAME, ID)

post_to_graph_data = {
    "date": today,
    "quantity": "100",
}

create_pixel_response = requests.post(
    url=post_to_graph_url, json=post_to_graph_data, headers=API_HEADER)


# update graph pixel
update_pixel_url = "https://pixe.la/v1/users/{}/graphs/{}/{}".format(
    USERNAME, ID, today)

update_pixel_data = {
    "quantity": "5000"
}

update_pixel_response = requests.put(
    url=update_pixel_url, json=update_pixel_data, headers=API_HEADER)

# Delete graph pixel
delete_pixel_url = "https://pixe.la/v1/users/{}/graphs/{}/{}".format(
    USERNAME, ID, today)

delete_pixel_response = requests.delete(
    url=delete_pixel_url, headers=API_HEADER)
print(delete_pixel_response.text)
