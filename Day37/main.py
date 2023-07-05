import requests

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

request = requests.post(url=creating_graph, json=graph_params, headers=headers)
print(request)
