import sys

def play_game():
    ## 1, 2, 3, GO!
    user_entry=0
    while user_entry != 1 and user_entry != 2: user_entry = input('Halp I need friends do you want to take my quiz?\n1. Yes\n2. No, sorry :(\nChoose 1 or 2: ')
    if user_entry == 2: print 'goodbye'
    while user_entry != 2:

        total_score = 0

        #QUESTION 1
        ans1 = input('Pick your favorite coffee drink\n1. Cortado\n2. A damn fine cup of coffee \n3. Almond milk latte\n4. I prefer tea\n\nYour answer: ')
        p1 = give_points(ans1)
        while p1 == -1:
            ans1 = input('INVALID INPUT. plz try again.\n\nYour answer: ')
            p1 = give_points(ans1)
        total_score += p1
        
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
    if points >= 5: print 'let us be friends\n'
    elif points < 5: ''

play_game()
