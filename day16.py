# from turtle import Turtle,Screen
# Timmy = Turtle()
# print(Timmy)
# Timmy.color("green")
# Timmy.shape(("turtle"))
# Timmy.pendown()
# Timmy.speed(10)
# for i in range(100):
#     Timmy.forward(100)
#     Timmy.right(40)

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align= "c"
print(table)