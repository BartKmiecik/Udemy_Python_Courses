from pprint import pprint
import requests
import os

os.environ['sheety_url'] = 'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/flightDeals/sheet1'
os.environ['sheety_author'] = 'Bearer secret'
SHEETY_PRICES_ENDPOINT = os.environ['sheety_url']

header = {
    'Authorization': 'Bearer secret'
}
class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
