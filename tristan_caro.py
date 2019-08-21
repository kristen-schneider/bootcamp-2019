import sys

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
		total_points = 0
		answer_one = input("Do you like coding? \n Yes or no? \n")
		## STEP 2&3 HERE
		
		## STEP 4 HERE
	
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	



####################################THE MASTER COMMENT
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
	bigdog = ["big", "Big"]
	fastprints("Do you like dogs? \n")
	command = input()
	if command in affirmatives:
		adder(5)
		fastprints("NICE. What kind? \n")
		command = input("Big or small dog? \n")
		if command in bigdog:
			adder(10)
			fastprints("Hell yeah \n Next Question \n")
			question2()
		elif command in smalldog:
			adder(5)
			fastprints("Cool cool \n Next Question \n")
			question2()
		else:
			fastprints("Not sure what kind of dog that is \n")
			question2()
	elif command in negatives:
		fastprints("Off to a bad start... but let's move on \n")
		question2()
	else:
		fastprints("I didn't understand that \n")
		question1()

def question2():
	fastprints("What is your favorite type of weather?\n")
	command = lower(input("Hot, cold, rainy, or idc\n"))
	if command == "hot":
		fastprints("I respect it \n")
		adder(5)
		question3()
	elif command == "cold":
		fastprints("Brrrrr\n")
		adder(10)
		question3()
	elif command == "rainy":
		fastprints()






initialize()
user()