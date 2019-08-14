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
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		## STEP 1 HERE
		answer_one = input('Do you like coding?\n1.Yes\n2. No\n\nYour Answer:')		
		## STEP 2&3 HERE
		if answer_one == 1:
			total_points += 5
		else:
			total_points += 0
		## STEP 4 HERE
		print total_points	
		
		#user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	


	
## Function call to play friendship algorithm game
play_game()
