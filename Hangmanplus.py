# Assignment 4
# Hangman Plus
# Anthony Swift


import random
WORDS = (	"PYTHON", "ESTIMATE", "DIFFICULT", "ANSWER", "XYLOPHONE", \
			"UNNECESSARY", "ADEQUATE", "FEASIBLE", "CHARACTER", \
			"CONGRATULATIONS", "SEQUENCE", "POSITION", "PROGRAM" )
MAX_WRONG = 6;
word = random.choice(WORDS)
so_far = "-" * len(word)
wrong = 0
used = []

def displayScaffold(wrong):

#Displays appropriate scaffold based on how many guesses the player has got wrong

 if wrong == 0:
  print("""
          ----------
          |/       |
          |
          |
          | 
          |
         ---
		 
         """)
		 
 if wrong == 1:
  print("""
          ----------
          |/       |
          |        0
          |
          | 
          |
         ---
		 
         """)
		 
 if wrong == 2:
  print("""
          ----------
          |/       |
          |        0
          |        |
          | 
          |
         ---
		 
         """)
		 
 if wrong == 3:
  print("""
          ----------
          |/       |
          |        0
          |       /|
          | 
          |
         ---
		 
         """)
		 
 if wrong == 4:
  print("""
          ----------
          |/       |
          |        0
          |       /|/
          | 
          |
         ---
		 
         """)
		 
 if wrong == 5:
  print("""
          ----------
          |/       |
          |        0
          |       /|/
          |       /
          |
         ---
		 
         """)
		 
 if wrong == 6:
  print("""
          ----------
          |/       |
          |        0
          |       /|/
          |       / /
          |
         ---
		 
         """)
    
print("\nWelcome to Hangman.")
displayScaffold(wrong)
print("\nYou have", MAX_WRONG, "wrong attempts to guess the word.")
while wrong < MAX_WRONG and so_far != word:
	print("\n", so_far, "\n")
	guess=input("Enter a letter: ")
	guess=guess.upper()
	while guess in used:
		print("\nYou have already guessed this letter\a", guess)
		guess=input("Enter a letter: ")
		guess=guess.upper()
	used.append(guess)
	if guess in word:
		print("\nYes,", guess, "is in the word.")
		displayScaffold(wrong)
		new=""
		for i in range(len(word)):
			if guess == word[i]:
				new += guess
			else:
				new += so_far[i]
		so_far = new
	else:
		print("\nSorry,", guess, "isn't in the word.\a")
		wrong += 1
		left = MAX_WRONG - wrong
		displayScaffold(wrong)
		print("\nYou have", left, "guesses left.")
if wrong == MAX_WRONG:
	print("\nYou've been hanged!\a")
else:
	print("\nYou guessed it!\a")
print("\nThe word was", word)
	