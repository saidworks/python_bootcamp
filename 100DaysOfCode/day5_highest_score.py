max = int(input("number of score to compare"))
scores = []
while len(scores) < max:
    entry = int(input("Enter the score of the subject"))
    scores.append(entry)
highest_number = 0
for i in scores:
    for j in scores:
            if i > j and i > highest_number:
                highest_number = i
print(highest_number)
