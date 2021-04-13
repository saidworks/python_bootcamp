#create list from each file text
with open('file1.txt' ,'r') as a:
    text = a.read()
    text = text.split()
    list_1=[int(i) for i in text]
with open('file2.txt' ,'r') as b:
    text = b.read()
    text = text.split()
    list_2=[int(i) for i in text]

#compare and add to new list
common_items = []
for i in list_1:
    for j in list_2:
        if i == j and (i not in common_items):
            common_items.append(i)

#play with dictionnaries
import random
import csv
with open("../nato_alphabet/nato_phonetic_alphabet.csv",newline="") as f:
    reader = csv.reader(f,delimiter=",")
    names = []
    for row in reader:
        names.append(row[1])

dict = {name:random.randint(1,100) for name in names}
passed_students = {name:score for name,score  in dict.items() if score>=60}
print(passed_students)

#build dictionary from a sentence and count letters from words
sentence = "What is the Airspeed Velocity of an Unladen Swallow"
letter_dict = {word:len(word) for word in sentence.split()}
# for word in sentence:
#     letter_dict[word] = len(word)

print(letter_dict)

# convert Celsius to fahreneit   f = 9/5*C + 32
import math
weather_c = {
    "day":"temperature",
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key:math.floor((9/5*value+32)) for key,value in weather_c.items() if type(value) != str}
print(weather_f)

# loop over dataframe
import pandas as pd
weather_frame= pd.Series(weather_c).to_frame()
print(weather_frame)

for (index,row) in weather_frame.iterrows():
    print(row)
for key,value in weather_frame.items():
    print(key,value)

weather_c_frame = pd.DataFrame(weather_c,index=[0])
print(weather_c_frame.day)