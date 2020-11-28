name1= input("enter your name please\n").lower() 
name2= input("enter his/her name\n").lower()
score1=name1.count("t")
score1+=name1.count("r")
score1+=name1.count("u")
score1+=name1.count("e")
score2=name2.count("l")
score2+=name2.count("o")
score2+=name2.count("v")
score2+=name2.count("e")
print("your score is",str(score1)+str(score2))

/*For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."*/

