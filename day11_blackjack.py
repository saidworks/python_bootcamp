import random 
from logo import blackjack
print(blackjack)
# player_cards = []
# dealer_cards = []

sum_player = 0
sum_dealer = 0 
play = True
ten = [10,"A","K","J","Q"]
def sum(list):
    sum = 0
    for i in list:
        sum += i
    return sum 
def display(list):
    display = []
    for i in list: 
        if i == 1:
            display.append("A")
        elif i == 10:
            display.append(random.choice(ten))
        else:
            display.append(str(i))
    return display


player_cards = [random.randint(1,10)]
computer_cards = [random.randint(1,10)]
while play:
    print("Your cards are :", display(player_cards))
    print("Dealer cards are :", display(computer_cards))
#hit
    player_choice = input("hit or stand? (h for hit or s for stand \t")
    if player_choice == "h":
        player_cards.append(random.randint(1,10))
        computer_cards.append(random.randint(1,10))     
        if sum(player_cards) > 21 and sum(computer_cards) <= 21 :
            print("Dealer cards are :", display(computer_cards))
            print("Your cards are :", display(player_cards))
            print("Dealer won his total is", sum(computer_cards))
            play = False
        elif sum(computer_cards) > 21 and sum(computer_cards) <= 21:
            print("Dealer cards are :", display(computer_cards))
            print("Your cards are :", display(player_cards))
            print("You won your total is", sum(player_cards)) 
            play = False
#stand
    elif player_choice == "s":
        computer_cards.append(random.randint(1,10))
        if sum(player_cards) <= 21 and sum(computer_cards) <= 21:
            if sum(computer_cards) > sum(player_cards):
                print("Dealer cards are :", display(computer_cards))
                print("Your cards are :", display(player_cards))
                print("Dealer won his total is", sum(computer_cards))
                play = False
            if sum(computer_cards) < sum(player_cards):
                print("Dealer cards are :", display(computer_cards))
                print("Your cards are :", display(player_cards))
                print("You won your total is", sum(player_cards)) 
                play = False
        


