#Assignment 2 - Guess The Word
#Anthony Swift

#Import the random library

import random

#Setup the word list

word_list = ["PYTHON", "GADGET", "SEQUENCE", "ROBOT"]

#Pick random word from the list

word = random.choice(word_list)

#Welcome player to the game

print("\nWelcome to the Guess The Word game\n")

#Display word with alternate letters
#If the letter in the word is odd, displays "-" in the word.
#If the letter in the word is even, displays the letter.

for x in range(0,len(word)):
 if x%2 == 0:
  print("-",end="")
 else:
  print(word[x],end="")

#Ask user to guess the word
print("\n")
guess = input("Please enter guess: ")

#Converts to uppercase if user enter guess in lowercase
guess = guess.upper()

#Check user guess. 
#If the user guesses the correct word, print a congratulations message.
#If the user does not guess the correct word, print loser message and display correct word.

if guess == word:
 print("\nCongratulations, you have guessed the correct word.")
else:
 print("\nYou have not guessed the correct word, you have lost the game")
 print("The correct word is", word)
 
 






