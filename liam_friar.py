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
                answer_one = input ("Have you ever kissed a squirrel?!\n1. Yes\n2. No\n\nYour Selection: ")
                ## STEP 2&3 HERE
                if int(answer_one) == 1:
                        total_points += 5
                else:
                        total_points -= 5
		
		answer_two = input ("Can you eat a rubick's cube in under 30 seconds?\n1. Yes\n2. No\n\nYour Selection: ")
		if int(answer_two) == 1:
			total_points += 5
		else:
			total_points -= 5


                ## STEP 4 HERE
                print "We are {}0 percent best friends".format(total_points)

                user_entry = input('Want to play again?!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')




## Function call to play friendship algorithm game
play_game()


