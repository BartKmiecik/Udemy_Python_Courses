import requests
import os

os.environ['tequile_api_key'] = 'YgQv2gWX8BR-IpYtW_KHXwHgp7WI6btz'
headers = {
    'apikey': os.environ['tequile_api_key']
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        key = os.environ['tequile_api_key']
        url = 'https://api.tequila.kiwi.com'
        location_query = '/locations/query'
        request = requests.get(url=f'{url}{location_query}', headers=headers)
        print(request)




search = FlightSearch()