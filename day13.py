############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# #fizbuzz game
# number = int(input("enter a number \t"))
# if number % 3 == 0 and number % 5 == 0:
#     print("FizBuzz")
# elif number % 3 == 0:
#     print("Fiz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0,5 )
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year >= 1981 and year <= 1996:
#   print("You are a millenial.")
# elif year > 1996:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(pages,word_per_page)
# print(total_words)

#Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    return b_list
  
print(mutate([1,2,3,5,8,13]))