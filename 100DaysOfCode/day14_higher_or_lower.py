from day14_data import logo,vs
from day14_data import data
import random 
score = 0
print(logo)
choice_1 = random.choice(data)
choice_2 = random.choice(data)
if choice_2 == choice_1:
    choice_2 = random.choice(data)

game_play = True
while game_play:
    # Define random choices to compare
    choice_1_name = choice_1["name"]
    choice_1_followers = choice_1['follower_count']
    choice_1_description = choice_1['description']
    choice_1_country = choice_1["country"]
    choice_2_name = choice_2["name"]
    choice_2_followers = choice_2['follower_count']
    choice_2_description = choice_2['description']
    choice_2_country = choice_2["country"]
    print(f"Compare 1 : {choice_1_name}, {choice_1_description} from {choice_1_country}")
    print(vs)
    print(f"Compare 2 : {choice_2_name}, {choice_2_description} from {choice_2_country}")
    user_choice = input("Who has more followers? type 1 or 2 \t") 
    if user_choice == "1":
        if choice_1_followers >= choice_2_followers:
            choice_1 = choice_1
            choice_2 = random.choice(data)
            score += 1
            print(f"{choice_1_name} have {choice_1_followers} ")
            print(f"{choice_2_name} have {choice_2_followers} ")
            print(f"you are right!  your score is {score}")
        else:
            print(f"{choice_1_name} have {choice_1_followers} ")
            print(f"{choice_2_name} have {choice_2_followers} ")
            print(f"you are wrong! your final score is {score}. Try again")
            game_play = False
    if user_choice == "2":
        if choice_2_followers >= choice_1_followers:
            choice_1 = choice_2
            choice_2 = random.choice(data)
            score += 1
            print(f"{choice_1_name} have {choice_1_followers} ")
            print(f"{choice_2_name} have {choice_2_followers} ")
            print(f"you are right!  your score is {score}")
        else:
            print(f"{choice_1_name} have {choice_1_followers} ")
            print(f"{choice_2_name} have {choice_2_followers} ")
            print(f"you are wrong! your final score is {score}. Try again")
            game_play = False



