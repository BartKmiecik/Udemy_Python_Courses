import requests

url = 'https://pixe.la/v1/users'

params = {
    'token': 'asdfxcvertdfsg',
    'username': 'bart32123',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
#
# request = requests.post(url=url, json=params)
print(request.text)
