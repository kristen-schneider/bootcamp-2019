import sys

## Function to play friendship algorithm game  
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	user_entry = int(user_entry)
	# ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 1 and user_entry != 2: user_entry = input("Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ")
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while user_entry == 1:
		
		total_points = 0

		## Question One
		answer_one = input("Do you h8 cats?\n1. Yes\n2. meh\n3. No, I love them!")
		answer_one = int(answer_one)

		if answer_one == 1:
			total_points += 0
			answer_oneone = input("Why do you h8 cats?\n1. I'm just not a great person\n2. jk! I do like cats. LOLZ.
			answer_oneone = int(answer_oneone)
				if answer_oneone == 1:
					total_points -= 5
				else:
					total_points += 2
		elif answer_one == 2: total_points += 2
		else: total_points += 5

		## Question Two
		answer_two = input("Do you like to hike?\n1. Yes\n2. No")
		answer_two = int(answer_two) 

		if answer_two == 1:
			total_points += 5
		else:
			total_points += 0
		
		## Question Three
		answer_three = input("Do you like country music?\n1. Yes\n2. No\n3. NO.")
		answer_three = int(answer_three)

		if answer_three == 1:
			total_points += 0
			answer_threeone = input("Why tho?\n1. Country music slaps!\n2. idk, I like listening to garbage I guess")
			answer_threeone = int(answer_threeone)
				if answer_threeone == 1:
					total_points -= 2
				else:
					total_points += 0
		elif answer_three == 2: total_points += 2
		else: total_points += 5		
				
		## The End
		if total_points >= 15: print("yesss, lets go take our cats on a hike!")
		elif total_points < 15 and total_points >= 9: print("frenz")
		elif total_points < 9 and total_points >= 5: print("maybe you're cool")
		else: ("plz try harder")
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	


	
## Function call to play friendship algorithm game
play_game()
