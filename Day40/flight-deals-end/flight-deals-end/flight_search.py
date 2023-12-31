import copy
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = 'YgQv2gWX8BR-IpYtW_KHXwHgp7WI6btz'


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        query2 = copy.deepcopy(query)
        query2['max_stopovers'] = 2
        query2['stop_over'] = 1
        query2['via_city'] = 'Shanghai'

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        response2 =  requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query2,
        )

        data = None
        try:

            data = response.json()["data"][0]
        except IndexError:
            print(f"No direct flights found for {destination_city_code}.")
            try:
                data = response2.json()["data"][0]
            except IndexError:
                print(f"No flights found for {destination_city_code}.")
        except KeyError:
            print(f'Corrupted date file')

        flight_data = None

        try:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"] if len(data['route']) < 3 else data["route"][1]["cityTo"],
                destination_airport=data["route"][0]["flyTo"] if len(data['route']) < 3 else data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
                stop_overs=0 if len(data['route']) < 3 else 1,
                via_city="" if len(data['route']) < 3 else data["route"][0]["cityTo"]
            )
            print(f"{flight_data.destination_city}: £{flight_data.price}")
        except UnboundLocalError:
            print('File has no value')
        except TypeError:
            print('NonType object, missing some data')

        return flight_data
