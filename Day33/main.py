import requests

parameters = {
    'lat': 50.0,
    'lng': 0.0,
    'formatted': 0
}


request = requests.get('https://api.sunrise-sunset.org/json', parameters)
result = request.json()['results']
sunrise = result['sunrise']
print(sunrise)