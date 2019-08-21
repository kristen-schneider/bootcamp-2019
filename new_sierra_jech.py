import sys

## Function to play friendship algorithm game  
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	# ask the user to make their own input (1 to play or 2 to exit):
	while int(user_entry) != 1 and int(user_entry) != 2: user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while int(user_entry) == 1:
		## Question 1
		total_points = 0
		answer_one = input("Do you prefer tea or coffee?\n1. tea\n2. cofee\n3. both\n")
		ansqer_one = int(answer_one)
		## Question 1 Points
		if answer_one == 1 : total_points += 5
		elif answer_one == 2 : total_points -= 5
		else: total_points += 2
		
		## Question 2
		answer_two = input("What is your favorite season of the year?\n1. summer\n2. fall\n3. winter\n4. spring\n5. all of 'em\n")
		answer_two = int(answer_two)
		## Question 2 Points
		if answer_two == 1 : total_points += 2
		elif answer_two == 2 : total_points += 2
		elif answer_two == 3 : total_points += 5
		elif answer_two == 4: total_points += 2
		else : total_points += 10

		## Question 3
		answer_three = input("The best coding is:\n1. python\n2. R\n3. C++ \n4. commented\n")
		answer_three = int(answer_three)

		## Question 3 Points
		if answer_three == 1: total_points += 5
		elif answer_three == 2: total_points += 5
		elif answer_three == 3: total_points += 2
		else : total_points += 10

		## Question 4
		answer_five = input("The best part of going to the Rayback is:\n1. corn hole\n2. dancing \n3. kombucha\n4. meeting my IQ peeps\n")
		answer_five = int(answer_five)

		## Question 4 Points
		if answer_five == 1: total_points += 2
		elif answer_five == 2: total_points += 2
		elif answer_five == 3: total_points += 5
		else : total_points += 5  

		## STEP 4 HERE
		if total_points >= 25: print("Let's write some commented code at the Rayback with kombucha or tea")
		elif total_points < 25 and total_points >= 14: print("why can't we be friends, why can't we be friends")
		else total_points < 14: print("ENEMIES!!!")
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)	

## Function call to play friendship algorithm game
play_game()
