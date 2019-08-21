"""import sys

## Function to play friendship algorithm game  
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	# ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 1 and user_entry != 2: user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while user_entry == 1:
		## STEP 1 HERE
		
		## STEP 2&3 HERE
	
		## STEP 4 HERE
	
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	


	
## Function call to play friendship algorithm game
play_game()
"""

import sys, time, random
import random

k = 0 #point counter
affirmatives = ["Yes", "yes", "Yeah", "yeah", "sure", "Sure"]
negatives = ["No", "no", "nope", "Nope"]

def adder(points):
	k += points
	return

def fastprints(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)

def initialize():
	fastprints("[###################")
	#time.sleep(3)
	fastprints("#")
	#time.sleep(3)
	fastprints("##")
	#time.sleep(3)
	fastprints("##############")
	fastprints("100%]")
	fastprints("\n...")
	fastprints("\n Welcome to Friendship Algorithm")

def user():
	fastprints("Do you want to take the quiz? \n")
	command = input()
	if command in affirmatives:
		fastprints("Great, let's get started \n")
		question1()
	elif command in negatives:
		fastprints("...Are you sure? \n")
		user()
	else:
		fastprints("Didn't understand that word \n")
		user()

def question1():
	fastprints("Do you like dogs? \n")
	command = input()
	if command in affirmatives:
		fastprints("NICE. What kind?")



initialize()
user()