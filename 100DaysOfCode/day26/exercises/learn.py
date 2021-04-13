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



