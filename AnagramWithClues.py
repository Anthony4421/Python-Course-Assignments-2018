# Assignment 3 - The Anagram Game with clues
#Anthony Swift
import random
WORDS =("python", "xylophone", "estimate", \
        "xylophone", "vauxhall", "orange")
clues = {"python" : "a programming language", "estimate" : "an educated guess", \
         "xylophone" : "a musical instrument", "vauxhall" : "a make of car", \
		 "orange" : "a type of fruit"}
# Choose a random word from the Word list
word = random.choice(WORDS)
correct = word
anagram = ""
# Mix up the letters in the word
for n in range(0, len(word)):
	position = random.randrange(len(word))
	anagram += word[position]
	word = word[:position] + word[(position+1):]
# Welcome the user, print the anagram, give the user a clue and get the first guess
print("\nWelcome to the anagram game.")
print("\nUnscramble the letters to make a word.")
print("\nThe anagram is:", anagram,"Clue: ",clues.get(correct))
answer = input("\nYour answer: ")
# Loop until the answer is correct or an empty string is input
while answer != correct and answer != "":
	print("\nSorry, that's not quite right.")
	answer = input("\nYour answer: ")
# The answer is correct
if answer == correct:
	print("\nWell done, you got it!")
