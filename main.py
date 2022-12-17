import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "subrath96"
TOKEN = "jhdhwjo22k3brkmdas23mrmsd"
GRAPH_ID = "graph1"
headers = {"X-USER-TOKEN": TOKEN}
today = datetime.now()
today_format = today.strftime("%Y%m%d")


# Creating a new user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# res = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(res.text)


# Creating a new Graph to represent data

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Daily Exercise",
    "unit": "minutes",
    "type": "int",
    "color": "shibafu",
}
# res = requests.post(url=graph_endpoint, json=graph_config, headers=headers)


# Updating graph Config using PUT method
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
put_confog = {"color": "sora"}
# res = requests.put(url=put_endpoint, json=put_confog, headers=headers)


# Updating graph values
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_format}"
update_config = {"quantity": "5"}
# res = requests.put(url=update_endpoint, json=update_config, headers=headers)


# Deleting graph value
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_format}"
# res = requests.delete(url=delete_endpoint, headers=headers)


# Pinning a graph in profile page
profile_endpoint = f"https://pixe.la/@{USERNAME}"
profile_config = {
    "displayName": "Subrath S",
    "title": "Software Developer",
    "timezone": "Asia/Kolkata",
    "aboutURL": "https://github.com/subraths",
    "pinnedGraphID": GRAPH_ID,
}
res = requests.put(url=profile_endpoint, json=profile_config, headers=headers)


# Adding values to graph
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Total Exercise today(minutes)? "),
}
# res = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(res.text)
