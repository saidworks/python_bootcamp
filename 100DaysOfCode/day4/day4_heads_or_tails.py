#Remember to use the random module 👇
import random




# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
chance = random.random()
if chance <= 0.5:
    print("heads")
else:
    print("tails")


