#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
i = random.randint(0,2)
chosen_word = word_list[i]
guesses = 0
#TODO-4 create an empty list called display to show letter and words at start it should be all hidden like _,_,_,_,_...

display = ["_" for i in range(len(chosen_word))]
while display != list(chosen_word):
    #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter from the hidden word ").lower()
    for j in range(len(chosen_word)):
        #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
        if guess == chosen_word[j]:
            print("right")
            display[j] = guess
        else:
            print("wrong")
    print(display)
    guesses += 1
    if guesses == len(chosen_word):
        print("You failed to save the man, game over")
        

