# Pixela documentation - https://docs.pixe.la/
from datetime import datetime
from numpy import delete
import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "velgrant"
TOKEN = "d1f65vc184981d4f"
GRAPH_ID = "graph1"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService":  "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params) //used to create an user account on pixela
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers) // Create a graph
# print(response.text)

pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")
pixel_post_config = {
    "date" : formatted_today, #  yyyyMMdd
    "quantity" : "5"
}

response = requests.post(
    url=pixel_post_endpoint,
    json=pixel_post_config,
    headers=headers
)
print(response.text)

edit_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_today}"
edit_config = {
    "quantity": "4.5"
}
# response = requests.put(url=edit_endpoint, json=edit_config, headers=headers) // edit the graph_data
# print(response.text)

delete_endpint = edit_endpoint
# response = requests.delete(url=delete_endpint, headers=headers) // delete the data
# print(response.text)