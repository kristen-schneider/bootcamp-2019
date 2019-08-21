import sys

#blah

def play_game():
	user_entry=0
	while user_entry == 0:
		user_entry = input('1:yes\n2:no\n\n')
	if user_entry == 2: 
		print('goodbye')
	while user_entry == 1:
		total_score = 0
	
		#QUESTIONS
		ans1 = input('Pick your favorite coffee drink\n1. Cortado\n2. A damn fine cup of coffee \n3. Almond milk latte\n4. I prefer tea\n\nYour answer: ')
		ans2 = input('What dinosaur as pet?\n1. duck-thing\n2. ptero\n3. stego\n4. parrot\n\nYour answer: ')       
		ans3 = input('Fill in the blank: grad school fills me with ______\n1. Knowledge\n2. I am empty inside\n3. Curiosity and wonder\n4. existensial dread\n\nYour answer: ')
		ans4 = input('Favorite life hack:\n1. napping\n2. Telling your mom you love her\3. Netflix\4. Pagan rituals\n\nYour answer: ')
		
		answers = [ans1,ans2,ans3,ans4]
		for ans in answers: 
			points = give_points(ans)
			while points == -1:
				ans = input('INVALID INPUT. plz try again.\n\nYour answer: ')
				points = give_points(ans1)
				total_score += points
        	
		#CALCULATE FRIENDSHIP
		calculate_friendship(total_score)
        	
        	# REPEAT MENU ITEM
		user_entry = input('Select Option!\n1. Play again\n2. Exit Game\n\nYour Selection: ')

def give_points(answer):
    q_points = 0
    if answer == 1: q_points += 10
    elif answer == 2: q_points += 5
    elif answer == 3: q_points += 0
    elif answer == 4: q_points -= -5
    else: q_points = -1

    return q_points

def calculate_friendship(points):
    if points >= 5: print('let us be friends\n')
    elif points < 5: ''

play_game()
