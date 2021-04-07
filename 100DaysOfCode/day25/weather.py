import csv

with open("weather_data.csv", "r", newline='') as datas:
    reader = csv.reader(datas, delimiter=',')
    weather_list = []
    for row in reader:
        weather_list.append(row)

