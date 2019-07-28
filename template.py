import sys
  
def play_game():
    
	## START GAME
    	user_entry = 0
    	while user_entry != 1 and user_entry != 2: user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
    	while user_entry == 1:

		## YOUR CODE HERE

        	## Q1, example
        	answer1 = input('Do you like coding?\n1. Yes\n2. No\n\nYour Answer: ')
		

		## REPEAT MENU ITEM
        	user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
play_game()
