import requests
from datetime import datetime

USERNAME = # Your username
TOKEN = # Your token here
GRAPH_ID = # Your Graph ID
DAY = datetime(year=2024, month=1, day=26)

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DAY.strftime('%Y%m%d')}"
DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DAY.strftime('%Y%m%d')}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Hrs",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

post_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you lear today? "),
}

response = requests.post(url=POST_PIXEL_ENDPOINT, json=post_pixel_config, headers=headers)
print(response.text)

update_pixel_config = {
    "quantity": "6.0",
}

# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_config, headers=headers)
# print(response.text)

# response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=headers)
# print(response.text)
