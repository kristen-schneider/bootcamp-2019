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
		if answer_one == "Yes":
			total_points += 2
		elif answer_one == 2: total_points += 5
		else:
			total_points += 1
		## STEP 4 HERE
		print(total_points)
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	



#Libraries
import sys, time, random
import random
#Global variables:
k = 0 #point counter
totalpossible = 50 #total possible points
username = ""
#Important lists:
affirmatives = ["Yes", "yes", "Yeah", "yeah", "sure", "Sure"]
negatives = ["No", "no", "nope", "Nope", "nah", "Nah"]
states = ["Maine","New Hampshire","Vermont","Massachusetts","Connecticut","Rhode Island","New York","New Jersey","Pennsylvania","Delaware","Maryland","Virginia","Florida","Texas","Kentucky","Tennessee","North Carolina","South Carolina","Georgia","Alabama","Mississippi","Arkansas","Louisiana","Missouri","Oklahoma","Ohio","Nebraska","Michigan","Indiana","Wisconsin","Illinois","Minnesota","Iowa","North Dakota","South Dakota","Kansas","Colorado","New Mexico","Arizona","Nevada","California","Wyoming","Montana","Utah","Idaho","Washington","Oregon","Alaska","Hawaii","West Virginia"]
floppydisk = "                 ' \n            *          .\n                   *       '\n              *                *\n\n\n\n\n\n   *   '*\n           *\n                *\n                       *\n               *\n                     *\n\n         .                      .\n         .                      ;\n         :                  - --+- -\n         !           .          !\n         |        .             .\n         |_         +\n      ,  | `.\n--- --+-<#>-+- ---  --  -\n      `._|_,'\n         T\n         |\n         !\n         :         . : \n         .       *\n"
def adder(points):
	global k 
	k += points
	return

def fastprints(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)

def slowprints(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

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
	fastprints("\nWelcome to Friendship Algorithm \n")
	global username
	username = input("What do you call yourself?\n")
	output = "Nice to meet you, {}\n".format(username)
	fastprints(output)

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
	command = input().lower()
	if command in affirmatives:
		adder(5)
		fastprints("NICE. What kind? \n")
		command2 = input("Big or small dog? \n").lower()
		if command2 == "big":
			adder(10)
			fastprints("Hell yeah \nNext Question \n")
			question2()
		elif command2 == "small":
			adder(5)
			fastprints("Cool cool \nNext Question \n")
			question2()
		else:
			fastprints("Not sure what kind of dog that is \n")
			question1()
	elif command in negatives:
		fastprints("Off to a bad start... but let's move on \n")
		question2()
	else:
		fastprints("I didn't understand that \n")
		question1()

def question2():
	fastprints("What is your favorite type of weather?\n")
	command = input("Hot, cold, rainy, or idc\n").lower()
	if command == "hot":
		fastprints("I respect it \n")
		adder(5)
		question3()
	elif command == "cold":
		fastprints("Brrrrr\n")
		adder(10)
		question3()
	elif command == "rainy":
		fastprints("oof alright\n")
		adder(5)
		question3()
	elif command == "idc":
		fastprints(".....k....\n")
		adder(5)
		question3()
	else:
		fastprints("I didn't understand that \n")
		question2()

def question3():
	fastprints("Are you excited for IQ Bio?\n")
	command = input().lower()
	if command in affirmatives:
		fastprints("Plus ten points!\n")
		adder(10)
		question4()
	elif command in negatives:
		fastprints("Are you sure about that?\n")
		command = input().lower()
		if command in affirmatives:
			fastprints("Minus ten points!\n")
			adder(-10)
			question4()
		elif command in negatives:
			fastprints("Ok... let's try this again\n")
			question3()
	else:
		fastprints("I didn't understand that \n")
		question3()

def question4():
	slowprints("Ok...\n")
	slowprints("Now...the most important question...\n")
	slowprints("What is ...\n")
	time.sleep(3)
	fastprints("YOUR FAVORITE ROCK?\n")
	command = input("Olivine\nBasalt\nSandstone\nI hate rocks\n").lower()
	if command == "olivine":
		adder(20)
		question5()
	elif command == "basalt":
		adder(15)
		question5()
	elif command == "sandstone":
		question5()
	else:
		fastprints("How dare you\n")
		question5()


def question5():
	fastprints("Ok last question. What is your favorite U.S. state?\n")
	command = input("")
	if command in states:
		output = "Alright, {} is a really cool state.\n".format(command)
		fastprints(output)
		tally(k,totalpossible)
	else:
		fastprints("I don't recognize that state\n")
		question5()

def tally(score,totalpossible):
	percentage = score/totalpossible*100
	fastprints(username)
	fastprints(", ready for your score?\n")
	command = input().lower()
	if command in affirmatives:
		fastprints("Here's your score:\n")
		scoregiver(percentage)
	elif command in negatives:
		fastprints("too bad! Here's your score:\n")
		scoregiver(percentage)
	else:
		fastprints("I don't understand\n")
		tally(score)

def scoregiver(perc):
	output = "{}'s has a {} percent friend fit, according to the friendship algorithm.\n".format(username, perc)
	fastprints(output)
	if perc >= 75:
		fastprints("Nice!\n\n\n")
		fastprints(floppydisk)
	elif perc >= 50:
		fastprints("Not bad!\n\n\n")
		fastprints(floppydisk)
	elif perc >= 25:
		fastprints("eh.. not great\n\n\n")
		fastprints(floppydisk)
	else:
		fastprints("Oof. Sorry buddy.\n\n\n")
		fastprints(floppydisk)

initialize()
user()