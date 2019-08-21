import sys

## Function to play friendship algorithm game  
def play_game():
	## START GAME

	# initialize the user input to 0
  user_entry = 0
	# ask the user to make their own input (1 to play or 2 to exit):
  while user_entry != 1 and user_entry != 2: 
    user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection:')
    user_entry = int(user_entry)
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
  while user_entry == 1:
		## STEP 1 HERE
    total_points = 0
    answer_one = input('Do you like to cook? \n1. Yes \n2. No \nYour Selection: ')
		## STEP 2&3 HERE
    if int(answer_one) == 1:
      answer_oneA = input('Do you prefer to \n1. Bake, or \n2. Use the stovetop? \nYour Selection: ')
      total_points += 5
    else:
      total_points += 0
		## STEP 4 HERE

    answer_two = input("Which is your favorite Harry Potter movie? \nEnter 1 through 8: ")
    answer_two = int(answer_two)
    if (answer_two == 3): total_points += 10
    elif (answer_two == 4): total_points += 5
    elif (answer_two == 7): total_points -=5

    answer_three = input("Do you like art? \n1. Yes \n2. No \nYour Selection: ")
    answer_three = int(answer_three)
    if (answer_three == 1):
      total_points += 5
      answer_threeA = input("Do you prefer \n1. Making it, or \n2. Observing it? \nYour Selection: ")
      answer_threeA = int(answer_threeA)
      if (answer_threeA == 1):
        total_points += 5
        answer_threeB = input("What is your favorite medium?\n1. Paint \n2. Sculpture \n3. Sketches \n4. Other \nYour Selection: ")
        answer_threeB = int(answer_threeB)
        if (answer_threeB == 1): total_points += 5
    else: total_points -= 5

    answer_four = input("Do you like to travel? \n1. Yes \n2. No \nYour Selection: ")
    answer_four = int(answer_four)
    if (answer_four == 1):
      total_points += 5
      answer_fourA = input("Would you rather go to \n1. Norway,  \n2. Indonesia, or \n3. Greece? \nYour Selection: ")
    else: total_points -= 5

    answer_five = input("What is your favorite book genre? \n1. Fantasy \n2. Romance \n3. Historical \nYour Selection: ")
    answer_five = int(answer_five)
    if (answer_five == 1): total_points += 5
    elif (answer_five == 2): total_points -= 5


    print (total_points)
    user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection:')
    user_entry = int(user_entry)
		
	


	
## Function call to play friendship algorithm game
play_game()
