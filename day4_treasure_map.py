# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
xy=list(position)
x,y=[int(i)-1 for i in xy]
print(x,y)
#Write your code above this row 👆
map[x][y]='x'
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")