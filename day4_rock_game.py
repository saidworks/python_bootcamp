import random

#variables
choices=["scissors","rock","paper"]

user_choice = input("Scissors, paper or rock\n")
computer_choice = random.choice(choices)

if user_choice == computer_choice:
    print("Draw!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("Computer had chosen ",computer_choice, " Computer won")
    else:
        print("You won")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("Computer had chosen ",computer_choice, " Computer won)
    else:
        print("You won")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Computer had chosen ",computer_choice, " Computer won)
    else:
        print("You won")