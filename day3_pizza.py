size=input("What size will be your pizza?") #s=small or m=medium or l=large
pepperoni = bool(input("would you like pepperoni"))  
cheese = bool(input("Would you like extra cheese"))
small_price = 15
medium_price = 20
large_price= 25
""" 

Pepperoni for Small Pizza: +$2
Pepperoni for Small Pizza: +$2

Pepperoni for Medium or Large Pizza: +$3
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1 """

if size == "s":
    if pepperoni:
        small_price += 2
    elif cheese:
        small_price += 1
    print(f"your bill is {small_price}")
elif size == "m":
    if pepperoni:
        medium_price += 3
    elif cheese: 
        medium_price += 1
    print(f"your bill is {medium_price}")
elif size == "l":
    if pepperoni:
        large_price += 3
    elif cheese:
        large_price += 1
    print(f"your bill is {large_price}")
