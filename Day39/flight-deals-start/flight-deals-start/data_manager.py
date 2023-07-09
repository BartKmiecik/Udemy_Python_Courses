import requests
import os


os.environ['sheety_url'] = 'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/flightDeals/sheet1'
os.environ['sheety_author'] = 'Bearer secret'

header = {
    'Authorization': 'Bearer secret'
}

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

    def add_user(self, user):
        id = self.check_row_id()
        request = requests.put(url=f'https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/flightDeals/users/{id}',json=user, headers=header)
        print(request.text)

    def check_row_id(self):
        request = requests.get(url='https://api.sheety.co/e623837db3ef07fc2dd590b5fd4f0822/flightDeals/users', headers=header)
        users_base = request.json()['users']
        ids = []
        for id in users_base:
            ids.append(int(id['id']))
        return ids

#
# date = {
#     'user':{
#         'firstName': 'Bart2',
#         'lastName': 'Kmie2',
#         'email': 'tttt2'
#     }
# }
#
# manager = DataManager()
# #
# last_id = max(manager.check_row_id())+1
# manager.update_date(date, last_id)