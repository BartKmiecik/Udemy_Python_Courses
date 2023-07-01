import pandas
import pandas as pd
#
# weather = pd.read_csv('weather_data.csv')
# print(weather)
# temp = weather['temp'].to_list()
# print(temp)

data = pandas.read_csv('Squirrel_Data.csv')
color_counts = data['Primary Fur Color'].value_counts()
print(color_counts)