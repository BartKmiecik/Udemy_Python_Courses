import requests
import os

os.environ['tequile_api_key'] = 'YgQv2gWX8BR-IpYtW_KHXwHgp7WI6btz'
headers = {
    'apikey': os.environ['tequile_api_key'],
}

pramas = {
    'fly_from': 'city:GDN',
    'date_from': '09/09/2023',
    'date_to': '09/10/2023',
    #'fly_to': 'PL'
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        #self.key = os.environ['tequile_api_key']
        self.url = 'https://api.tequila.kiwi.com'
        #location_query = '/locations/query'
        # request = requests.get(url=f'{self.url}/v2/search', params= pramas,headers=headers).json()
        # country = request['data'][0]['countryTo']
        # price = request['data'][0]['price']
        # print(country, price)

    def check_flight_price(self, destination: str = None):
        """
        destination exp: PL, FRA 'fly_to=city:DUS' will match all airports in "DUS", "MGL" and "NRN" (all in the city of Duesseldorf)
'fly_to=airport:DUS' will only match airport "DUS"
        """
        pramas = {
            'fly_from': 'city:GDN',
            'date_from': '09/09/2023',
            'date_to': '09/10/2023',
        }
        if destination:
            pramas['fly_to'] = destination

        request = requests.get(url=f'{self.url}/v2/search', params=pramas, headers=headers).json()
        country = request['data'][0]['countryTo']
        price = request['data'][0]['price']
        #print(country, price)
        return price

# search = FlightSearch()
# search.check_flight_price('QWE')
