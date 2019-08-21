import sys

## Function to play friendship algorithm game  
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	user_entry = int(user_entry)
	# ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 1 and user_entry != 2: user_entry = int(input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while int(user_entry) == 1:
		## STEP 1 HERE
		total_points = 0
		answer_one = int(input("Do you like dogs?\n1. Yes\n2. No\n"))
		## STEP 2&3 HERE
		if answer_one == 1: total_points += 5 
		else: total_points += 0
		## STEP 4 HERE
		print(total_points)

		#question 2
		answer_two = int(input("Cheez its or Goldfish?\n1. Cheez its\n2. Goldfish\n3. I don't like orange snacks\n"))
		if answer_two == 2: total_points += 5
		elif answer_two == 1: total_points += 0
		else: total_points -= 5
		print(total_points)
		
		#question 3
		answer_three = int(input("You have a sunny day off! What do you do?\n1. Go outside\n2. I hate sunlight\n"))
		if answer_three == 1: 
			total_points += 20
			#conditional question 4
			answer_four = int(input("Where are adventuring today?\n1. To the mountains!\n2. Playing sports!\n3. By a lake with a book\n4. TBD\n"))
			if answer_four == 1: print("Ski/hike buddy!")
			elif answer_four == 2: print("Want to join my team?")
			elif answer_four == 3: print("I like books too.")
			else: print("let's go!") 
		else: total_points -= 20

		print("Your score: ")
		print(total_points)

		if total_points > 20: print("Besties!")
		elif total_points > 5: print("we've got potential")
		else: print("any other hobbies?") 
	
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)



	
## Function call to play friendship algorithm game
play_game()
