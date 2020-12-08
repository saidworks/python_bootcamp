import random

guesses = 0

def choose_level(level):
    if level == "hard":
        return  5
    elif level == "medium":
        return  7
    elif level == "easy":
        return  10
difficulty = input("Choose level : hard , medium or easy \t")
guesses = choose_level(difficulty)
number = random.randint(1,100)
while guesses > 0 :

    
    guess = int(input("try to guess the number chosen by the computer between 1 and 100 \t"))
    guesses -= 1
    if guess == number:
        print(f"congratulations you guessed right! the number is {number}")
        guesses = 0
    elif guess < number:
        print("Your guess is smaller than the number")
        print("You have {} remaining".format(guesses))
    elif guess > number:
        print("your guess is bigger than the number")
        print("You have {} remaining".format(guesses))
    else:
        print("your number is not within range")
    
    if guesses == 0 and guess != number:
        print("game over! try again")