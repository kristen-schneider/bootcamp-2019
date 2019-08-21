import sys

## Function to play friendship algorithm game  
def play_game():
    ## START GAME

    # initialize the user input to 0
    user_entry = 0
    # ask the user to make their own input (1 to play or 2 to exit):
    while user_entry != 1 and user_entry != 2:
        user_entry = int(input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))
    while user_entry == 1:
        ## STEP 1 HERE
        total_points = 0
        answer_one = int(input("Which TV Show is better?\n1. Friends\n2. How I Met Your Mother\n3. I don't like either\n4. I can't decide\n5. I haven't seen either\n"))
        ## STEP 2&3 HERE
        if answer_one == 1: total_points += 4
        elif answer_one == 2: total_points += 0
        elif answer_one == 3: total_points -= 4
        elif answer_one == 4: total_points += 2
        else: total_points -= 2
	## STEP 4 HERE
        # print(total_points)
		
         ## STEP 1 HERE
        answer_two = int(input("How do you feel about kombucha?\n1. LOVE \n2. It's fine\n3. it's gross\n4. what is kombucha?\n5. it's SUPER gross\n"))
        ## STEP 2&3 HERE
        if answer_two == 1: total_points += 4
        elif answer_two == 2: total_points += 2
        elif answer_two == 3: total_points -= 2
        elif answer_two == 4: total_points -= 2
        else: total_points -= 4
        ## STEP 4 HERE
        # print(total_points)
        
        ## STEP 1 HERE
        answer_three = int(input("Do you like to hike?\n1. yes\n2. kinda \n3. naw not really my thing\n4. absolutely not\n"))
        ## STEP 2&3 HERE
        if answer_three == 1: total_points += 4
        elif answer_three == 2: total_points += 2
        elif answer_three == 3: total_points -= 2
        else: total_points -= 4
        ## STEP 4 HERE
        # print(total_points)

        if answer_three == 1:
            answer_four = int(input("what is your general hiking attitude?\n1. let's RUN up the mountain\n2. I like a good workout but let's not die\n3. pretty leisurely\n4. not a lot of hiking, BUT let's take a million pictures\n"))
            if answer_four == 1: total_points += 0
            elif answer_four == 2: total_points += 4
            elif answer_four == 3: total_points +=2
            else: total_points -= 4

        answer_five = int(input("Do you like dogs?\n1. yes\n2. kinda\n3. no"))
        if answer_five == 1: total_points += 4
        elif answer_five == 2: total_points += 2
        else: total_points -= 4
        # print(total_points)

        ##  Find out if you can be friends!!
        if total_points >= 10: print("\nYAY best friend material")
        elif total_points >= 6: print("\nsweeeeeeeeet we can be friends!")
        else: print("\n Yikes friendship could be rough\n")

        user_entry = input('\nSelect Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	


	
## Function call to play friendship algorithm game
play_game()
