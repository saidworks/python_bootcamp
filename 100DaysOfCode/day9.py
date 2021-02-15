from day9_logo import logo 

print(logo)
#dictionnaries challenge blind-auction
#I should add another functionnality if the numbers of bidders in unknown

total = int(input("please enter the total number of bidder"))
i = 0
dictionnary = {} 
biggest_bid = 0
def find_biggest_bid(dictionnary):
    global biggest_bid
    for i in dictionnary.values():
        for j in dictionnary.values():
            if i > j and i > biggest_bid:
                biggest_bid = i
        
    for key,value in dictionnary.items():
        if value == biggest_bid:
            print(f"The winner is {key} with a bid of {value}")
while i < total: 
    name = input("enter your name please \n")
    bid = float(input("enter your bid please \n"))
    dictionnary[name] = bid
    find_biggest_bid(dictionnary)
    i += 1


    
