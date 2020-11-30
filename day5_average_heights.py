# 🚨 Don't change the code below 👇
students_heights=[]
height_entry=""
while height_entry != "exit":
  height_entry = input("Input a student's height please, when you are done enter exit \n ")
  if height_entry != "exit":
    students_heights.append(height_entry)
  
for n in range(0, len(students_heights)):
  students_heights[n] = int(students_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum = 0
for i in students_heights:
     sum += i
average = sum / len(students_heights)
print(average)




