import requests
import os

os.environ['tequile_api_key'] = 'YgQv2gWX8BR-IpYtW_KHXwHgp7WI6btz'
headers = {
    'apikey': os.environ['tequile_api_key'],
}

pramas = {
    'fly_from': 'FRA',
    'date_from': '09/09/2023',
    'date_to': '10/10/2023',
    'fly_to': 'PL'
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        key = os.environ['tequile_api_key']
        url = 'https://api.tequila.kiwi.com'
        location_query = '/locations/query'
        request = requests.get(url=f'{url}/v2/search', params= pramas,headers=headers)
        print(request.json())




search = FlightSearch()