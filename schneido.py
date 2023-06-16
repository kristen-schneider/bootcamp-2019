import sys

def play_game():
    ## START GAME
    user_entry = 0
    while user_entry != 1 and user_entry != 2: user_entry = int(input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))
    while user_entry == 1:
    
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
                        '3. Drake\n4. I hate rap.\n\nYour Answer: ')
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
                        '3. France\n4. I said I hate cities!\n\nYour Answer: ')
        p8 = give_points(answer8)
        while p8 == -1:
            answer8 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p8 = give_points(answer8)
        total_points += p8
        
        ## QUESTION 9
        answer9 = input('You are going on a top secret mission--who do you employ as a team?\n1. The Tune Squad.\n2. Winnie the Pooh & friends.\n'
                        '3. Your best friends.\n4. I hate top secret missions.\n\nYour Answer: ')
        p9 = give_points(answer9)
        while p9 == -1:
            answer9 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p9 = give_points(answer9)
        total_points += p9
        
        ## QUESTION 10
        answer10 = input('Which female Disney villain is the best?\n1. Malificent.\n2. Yzma\n'
                        '3. Cruella de Vil \n4. I hate female Disney villains.\n\nYour Answer: ')
        p10 = give_points(answer10)
        while p10 == -1:
            answer10 = input('INVALID INPUT. Try again.\n\nYour Answer: ')
            p10 = give_points(answer10)
        total_points += p10
        
        
        print('You\'ve completed my friendship algorithm! Thanks for playing!\nRESULTS: ' + str(total_points) + '/110.')
        calculate_friendship(total_points)
        
        ## REPEAT MENU ITEM
        user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
    
def give_points(answer):
        answer = int(answer)
        q_points = 0
        if answer == 1: q_points += 10
        elif answer == 2: q_points += 5
        elif answer == 3: q_points += 0
        elif answer == 4: q_points -= 5
        else: q_points = -1

        return q_points

def calculate_friendship(points):
        if points >= 85: print('We are gonna be TIGHT. Boys for LIFE!!!!\n\n')
        elif points < 85 and points >= 50: print('You\'re pretty chill. Or MAYBE you\'re insane. Either way. I\'m into it.\n\n')
        elif points < 50 and points >= 20: print('Ya. We different, but we sometimes the same. Could be a fun balancing act?\n\n')
        elif points < 20 and points >= 0: print('I\'m sure we could find SOMETHING we have in common. Eventually.\n\n')
        else: print('So we\'re REALLY different !! That\'s cool I guess!.. ..!!.. !.\n\n')

play_game()



