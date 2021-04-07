# import csv
# using csv get temperatures of the week
# with open("weather_data.csv", "r", newline='') as datas:
#     reader = csv.reader(datas, delimiter=',')
#     weather_list = []
#     for row in reader:
#         if row[1] != "temp":
#             weather_list.append(row[1])

import pandas as pd
#open the data using pandas
data = pd.read_csv("weather_data.csv")
#get data in columns
print(data["temp"])
data_dict = data.to_dict()
print(data_dict)
temp_list = data['temp'].to_list()
print(temp_list)
sum = 0
for i in temp_list:
    sum += i
avg_temp = sum / len(temp_list)
print(avg_temp)
print(data['temp'].mean())
print(data['temp'].max())
#pandas convert datas to object where columns are properties
print(data.condition)
#get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

Monday = data[data.day == "Monday"]
print(Monday.temp)
# °F = (0°C × 9/5) + 32
Monday_temp = Monday.temp*9/5 + 32
print(Monday_temp)

#create a dataframe from scratch
raw_data = {
    "students": ["Amy",'James',"Angela"],
    "scores": [76, 56, 65]
}
new_data = pd.DataFrame(raw_data)
new_data.to_csv("new_data.csv")




