#Assignment 8
#Find The Diamond Game
#Anthony Swift

#Import modules

from tkinter import *
import tkinter.messagebox as msgBox
import random
import sys


#Declare variables to store randomly generated box number and number of guesses

global number_of_guesses
global random_box_number

#Set the window properties

window = Tk()
window.title("Find The Diamond")
window.configure(bg = "plum")
window.resizable(0,0)

# Create the widgets:

box1Btn = Button(window, width=10, height=3)
box2Btn = Button(window, width=10, height=3)
box3Btn = Button(window, width=10, height=3)
box4Btn = Button(window, width=10, height=3)
box5Btn = Button(window, width=10, height=3)
box6Btn = Button(window, width=10, height=3)
box7Btn = Button(window, width=10, height=3)
box8Btn = Button(window, width=10, height=3)
box9Btn = Button(window, width=10, height=3)
box10Btn = Button(window, width=10, height=3)

hideBtn = Button(window)

instructions = Label(window, wraplength=300, anchor=W, justify="left")

# Specify the grid layout:

box1Btn.grid(row=0, column=0, padx=10, pady=10)
box2Btn.grid(row=0, column=1, padx=10, pady=10)
box3Btn.grid(row=0, column=2, padx=10, pady=10)
box4Btn.grid(row=0, column=3, padx=10, pady=10)
box5Btn.grid(row=0, column=4, padx=10, pady=10)
box6Btn.grid(row=1, column=0, padx=10, pady=10)
box7Btn.grid(row=1, column=1, padx=10, pady=10)
box8Btn.grid(row=1, column=2, padx=10, pady=10)
box9Btn.grid(row=1, column=3, padx=10, pady=10)
box10Btn.grid(row=1, column=4, padx=10, pady=10)
hideBtn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
instructions.grid(row=2, column=2, columnspan=3, padx=10, pady=10)

#Declared function for each of the 10 buttons
#Passes the box number to the checkguess function when user clicks the button

def button1():
 box_number = 1
 box_number = checkguess(box_number)
 
def button2():
 box_number = 2
 box_number = checkguess(box_number)
 
def button3():
 box_number = 3
 box_number = checkguess(box_number)
 
def button4():
 box_number = 4
 box_number = checkguess(box_number)
 
def button5():
 box_number = 5
 box_number = checkguess(box_number)
 
def button6():
 box_number = 6
 box_number = checkguess(box_number)

def button7():
 box_number = 7
 box_number = checkguess(box_number)
 
def button8():
 box_number = 8
 box_number = checkguess(box_number)
 
def button9():
 box_number = 9
 box_number = checkguess(box_number)
 
def button10():
 box_number = 10
 box_number = checkguess(box_number)

#When user clicks hide diamond button
#Enables the 10 box buttons
#and disables the hide diamond button
#Lets the user know the diamond has been hideen

def hide_diamond():
 #Declare the variables to store randomly generatede box number and number of guesses
 
 global random_box_number
 global number_of_guesses
 
 #Set number of guesses to 0.
 
 number_of_guesses = 0
 
 #Generate random box number
 
 random_box_number = random.randint(1,10)
 
 #Prints the random box number to the console
 #I have added this for testing purposes
 print(random_box_number)
 
 #Allow the boxes to be clicked by player
 
 box1Btn.configure(state=NORMAL)
 box2Btn.configure(state=NORMAL)
 box3Btn.configure(state=NORMAL)
 box4Btn.configure(state=NORMAL)
 box5Btn.configure(state=NORMAL)
 box6Btn.configure(state=NORMAL)
 box7Btn.configure(state=NORMAL)
 box8Btn.configure(state=NORMAL)
 box9Btn.configure(state=NORMAL)
 box10Btn.configure(state=NORMAL)
 
 #Disbale the hide diamond button
 
 hideBtn.configure(state=DISABLED)
 
 #Display message to let user know the diamond has been hidden
 
 msgBox.showinfo(" ","The diamond has been hidden")
 

#Configure each of the buttons so that they are disabled at start of game
#until hide the diamond button is clicked

#Each button will call the appropriate button function 
#which passes the value to the checkguess function

box1Btn.configure(text="1", bg="yellow", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button1)
box2Btn.configure(text="2", bg="blue", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button2)
box3Btn.configure(text="3", bg="brown", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button3)
box4Btn.configure(text="4", bg="dark green", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button4)
box5Btn.configure(text="5", bg="red", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button5)
box6Btn.configure(text="6", bg="purple", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button6)
box7Btn.configure(text="7", bg="black", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button7)
box8Btn.configure(text="8", bg="grey", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button8)
box9Btn.configure(text="9", bg="dark blue", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button9)
box10Btn.configure(text="10", bg="pink", fg="white", \
					padx=10, pady=10, border=3, state=DISABLED, command=button10)
hideBtn.configure(text="Hide The Diamond", bg="light sea green", fg="white", \
					padx=10, pady=10, border=3, command=hide_diamond)
instructions.configure(bg="plum", padx=10, pady=10, text="Click the Hide The Diamond Button to start the game. Then, click on the box where you think the diamond is hidden. You have three guesses to find it.")  



 
def checkguess(box_number):

#This function checks the box clicked by the player
#and displays message to inform player whether they have clicked the correct box

#Declare variables 
 global random_box_number
 global number_of_guesses
 
#If the box number clicked by player is equal to random number generated
#Congratulate player and ask if they would like to play again

 if box_number == random_box_number:
  msgBox.showinfo("Congratulations", "Congratulations! You have found the diamond.")
  yesNo = msgBox.askquestion(" ", "Would you like to play again?")
  
#If player clicks they would like to play again
#Calls the hide diamond function and restarts the game
#Otherwise the game will exit

  if yesNo == "yes":
   hide_diamond()
  else:
   exit()
 else:
 
#If box number clicked by player does not match the random number generated
#Adds 1 to number of guesses

  number_of_guesses +=1
  
 #If number of guesses less than 3
 #displays message to let player know their guess was incorrect
 #else - prints message to let player know they are out of guesses and prints correct box number
 #asks player if they would like to play again
 
  if number_of_guesses < 3:
   msgBox.showinfo("Incorrect","The guess was wrong")
  else:
   msgBox.showinfo("Game Over","You are out of guesses. The diamond was in box " + str(random_box_number))
   yesNo = msgBox.askquestion(" ", "Would you like to play again?")
   
   #If player clicks they would like to play again
   #Calls the hide diamond function and restarts the game
   #Otherwise the game will exit
   
   if yesNo == "yes":
    hide_diamond()
   else:
    exit()
  





# Sustain window:
window.mainloop()


