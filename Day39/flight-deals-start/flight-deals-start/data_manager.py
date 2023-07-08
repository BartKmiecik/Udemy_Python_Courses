import requests
import os

os.environ['sheety_url'] = 'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/flightDeals/sheet1'
os.environ['sheety_author'] = 'Bearer secret'
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = os.environ['sheety_url']
        self.headers = {
            'Authorization': os.environ['sheety_author']
        }

    def get_date(self):
        self.request = requests.get(url=self.url, headers=self.headers)
        city_price = []
        for n in self.request.json()['sheet1']:
            combo = (n['city'], n['iataCode'], n['lowestPrice'])
            city_price.append(combo)
        # print(self.request.json()['sheet1'])
        return city_price

