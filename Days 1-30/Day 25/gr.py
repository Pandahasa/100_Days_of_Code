import csv
import os
import sys
a = os.path.join(sys.path[0], 'weather_data.csv')


import pandas

data = pandas.read_csv(a)

data_dict = data.to_dict()

print(data_dict)

temp_list = data["temp"].to_list()

average = sum(temp_list) / len(temp_list)

print(f"highest temperature: {data['temp']}")