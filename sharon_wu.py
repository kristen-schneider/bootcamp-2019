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
		q1 = input("Do you enjoy reading books?\n1: Yes\n2: No")
		try:
			q1 = int(q1)
		except Exception as e:
			raise ValueError("Answer must be an integer!")

		## STEP 2&3 HERE
		if q1 == 1:
			total_points += 10
		else:
			total_points -= 5

		## STEP 4 HERE


		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')




## Function call to play friendship algorithm game
play_game()
