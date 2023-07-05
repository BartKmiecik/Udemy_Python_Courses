import requests
from datetime import datetime as dt

url = 'https://pixe.la/v1/users'
username = 'bart32123'
token = 'asdfxcvertdfsg'
headers = {
    'X-USER-TOKEN': token
}

params = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
#
# request = requests.post(url=url, json=params)
# print(request.text)

creating_graph = f'{url}/{username}/graphs'

graph_params = {
    'id': 'graph1',
    'name': 'myGraph1',
    'unit': 'fucks',
    'type': 'float',
    'color': 'momiji'
}

# request = requests.post(url=creating_graph, json=graph_params, headers=headers)
# print(request)

post_pixel = f'{creating_graph}/graph1'

now = dt.now()

pixel_params ={
    'date': now.strftime('%Y%m%d'),
    'quantity': '9'
}

# print(pixel_params)

update_pixel = f'{post_pixel}/{now.strftime("%Y%m%d")}'

update_params ={
    'quantity': '19'
}

delete_pixel = f'{update_pixel}'

request = requests.delete(url=delete_pixel, headers=headers)
print(request)

