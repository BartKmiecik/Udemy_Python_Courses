import pandas as pd

weather = pd.read_csv('weather_data.csv')
print(weather)
temp = weather['temp'].to_list()
print(temp)