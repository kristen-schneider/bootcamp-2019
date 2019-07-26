import sys

def play_game():
    ## START GAME
    user_entry = 0
    while user_entry != 1 and user_entry != 2: user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
    while user_entry != 2:

        ## KEEP TRACK OF POINTS
        total_points = 0

        ## QUESTION 1
        answer1 = input('Do you like to play sports?\n1. Yes, all of them!\n2. Yes, but only specific ones.\n'
                        '3. Some, but I would prefer to do other things.\n4. I hate them.\n\nYour Answer: ')
        p1 = give_points(answer1)
        while p1 == -1:
            answer1 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p1 = give_points(answer1)
        total_points += p1

        ## QUESTION 2
        answer2 = input('Do you like dogs, cats, or some other animal most (as a pet)?\n1. Dogs!\n2. Cats!\n'
                        '3. Other pet!\n4. I hate pets.\n\nYour Answer: ')
        p2 = give_points(answer2)
        while p2 == -1:
            answer2 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p2 = give_points(answer2)
        total_points += p2

        ## QUESTION 3
        answer3 = input('What most describes your sense of humor?\n1. I am here for a silly goose time and that\'s it!\n2. Sarcastic!\n'
                        '3. I love puns!\n4. I hate humor.\n\nYour Answer: ')
        p3 = give_points(answer3)
        while p3 == -1:
            answer3 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p3 = give_points(answer3)
        total_points += p3

        ## QUESTION 4
        answer4 = input('Quick! Pick a fruit.\n1. Apple\n2. Banana\n'
                        '3. Peach\n4. I hate fruit.\n\nYour Answer: ')
        p4 = give_points(answer4)
        while p4 == -1:
            answer4 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p4 = give_points(answer4)
        total_points += p4


	## QUESTION 5
        answer5 = input('A vegetable?\n1. ALL OF THEM!\n2. Broccoli\n'
                        '3. Cabbage\n4. I hate vegetables.\n\nYour Answer: ')
        p5 = give_points(answer5)
        while p5 == -1:
            answer5 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p5 = give_points(answer5)
        total_points += p5

	## QUESTION 6
        answer6 = input('Who is the best rapper of all time.\n1. Marshall Bruce Mathers III.\n2. Kendrick Lamar\n'
                        '3. MGK\n4. I hate rap.\n\nYour Answer: ')
        p6 = give_points(answer6)
        while p6 == -1:
            answer4 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p6 = give_points(answer6)
        total_points += p6

	## QUESTION 7
        answer7_a = input('If you could live in any city in the US, where would you live?\n1. Chicago\n2. NYC\n'
                        '3. Denver\n4. I hate cities.\n\nYour Answer: ')
        p7_a = give_points(answer7_a)
        while p7_a == -1:
            answer7_a = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p7_a = give_points(answer7_a)
        total_points += p7_a
	if answer7_a == 1:
		answer7_b = input('Where are we going for deep dish?\n1. Gio\'s\n2. Lou\'s\n'
                        '3. Wherever, I guess.\n4. I hate deep dish.\n\nYour Answer: ')
		p7_b = give_points(answer7_b)
        	while p7_b == -1:
            		answer7_b = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            	p7_b = give_points(answer7_b)
        	total_points += p7_b


	## QUESTION 8
	answer8 = input('If you could live in any city outside the US, where would you live?\n1. Mexico City\n2. Rio de Janeiro\n'
                        '3. Denver\n4. I said I hate cities!\n\nYour Answer: ')
	p8 = give_points(answer8)
        while p8 == -1:
            answer8 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p8 = give_points(answer8)
        total_points += p8


        ## REPEAT MENU ITEM
        user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')

def give_points(answer):
    q_points = 0
    if answer == 1: q_points += 10
    elif answer == 2: q_points += 5
    elif answer == 3: q_points += 0
    elif answer == 4: q_points -= -5
    else: q_points = -1

    return q_points

def calculate_friendship(points):
    if points >= 80: print 'We are gonna be TIGHT. Boys for LIFE!!!!'
    elif points < 80 and points >=60: ''

play_game()



