from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import  NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
notificator = NotificationManager()
city_price = data_manager.get_date()
print(city_price)
notificator.send_notification('test')
for city in city_price:
    flight_price = flight_search.check_flight_price(city[1])
    try:
        if flight_price < city[2]:
            msg = f'Price for flight to {city[0]} is now {flight_price}'
            notificator.send_notification(msg)
    except TypeError:
        print('Something doesn\'t import correctly from google sheet, just ignore. ')