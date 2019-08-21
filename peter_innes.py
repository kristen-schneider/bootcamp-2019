import sys

#blah

def play_game():
	user_entry=0
	while user_entry == 0: user_entry = input('Do you want to take my friendship quiz? Yes or No.\n ')
	if user_entry == "No": print('goodbye')
	while user_entry == "Yes":
		total_score = 0

		# QUESTIONS
		ans1 = input('Pick your favorite coffee drink\n1. Cappucino\n2. A damn fine cup of coffee \n3. Caffeine makes me anxious\n4. I prefer tea\n\nYour answer: ')
			
		
		ans2 = input('What dinosaur as pet?\n1. duck-thing\n2. parrot\n3. stego\n4. pterodactyl\n\nYour answer: ')       
		
		if int(ans2) == 1: 
			ans2b = input('What do ducks mean to you?\n1. duck is life\n2. I eat the duck\n3. Mighty Ducks is a great movie\n4. I go to the duck park daily\n\nYour answer: ')
			if int(ans2b) == 4: total_score +=10
			else: total_score +=5
	
		ans3 = input('Fill in the blank: grad school fills me with ______\n1. Curiosity and Wonder\n2. I am empty inside\n3. Knowledge\n4. existensial dread\n\nYour answer: ')
		ans4 = input('Favorite life hack:\n1. Napping\n2. Telling your mom you love her\n3. Bubble baths\n4. Pagan rituals\n\nYour answer: ')
		
		# LOOP THROUGH ANSWERS AND GIVE POINTS
		answers = [ans1, ans2, ans3, ans4]
		for answer in answers: 
			points = give_points(answer)
			total_score += points
		
		# CALCULATE FRIENDSHIP
		calculate_friendship(total_score)
        	
        	# REPEAT MENU
		user_entry = input('Select Option!\n1. Play again?\nYes or No:\n')

def give_points(answer):
	answer=int(answer)
	points = 0
	if answer == 1: points += 7
	elif answer == 2: points += 10
	elif answer == 3: points += 6
	elif answer == 4: points -= 5
	return points

def calculate_friendship(total_score):
	print('your score is:', total_score, 'out of 50')
	if total_score >= 5: print('let us be friends\n')
	elif total_score < 5: print('yay friends\n')

play_game()
