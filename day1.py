
from random import *
#1. Create a greeting for your program.
name = input("enter your name please")
print("welcome to the band name generator",name)
#2. Ask the user for the city that they grew up in.
city =input("Please enter your city?")
#3. Ask the user for the name of a pet.
pet = input("Please enter name of your pet")
#4. Combine the name of their city and pet and show them their band name.
band_name = pet + city + str(randint(0,10))  
#5. Make sure the input cursor shows on a new line, see the example at:
print(band_name)
#   https://band-name-generator-end.appbrewery.repl.run/