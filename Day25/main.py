import pandas as pd
import numpy as np

weather = pd.read_csv('weather_data.csv')
print(weather)
temp = weather['temp'].to_numpy()
print(temp)