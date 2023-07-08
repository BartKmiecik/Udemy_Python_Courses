from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import  NotificationManager
#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

city_price = data_manager.get_date()
print(city_price)
for city in city_price:
    flight_price = flight_search.check_flight_price(city[1])
    print(f'Price for flight to {city[0]} is now {flight_price}')