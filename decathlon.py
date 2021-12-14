print("Welcome to the 2021 Decathlon!")
print("We have two games to choose from!")
game = 0 #which game the user wants to play
print("1----Long-Jump")
print("2----110 Metre Hurdles")
game = int(input("Which game would you like to start with? "))
if game == 1:
    print("You have chosen Long-Jump!")
    import random
    attempts = 3 #attempts the user has
    failed = False #if the make a bad attempt
    freeze = [] #frozen dice
    def roll(num): #rolls the remaining dice
        dice = [] #dice that can be rolled
        for i in range(num):
            D = random.randint(1, 6)
            dice = dice + [D]
        return dice

    def nice_list(var): # makes the dice pretty!!!
        nice = []
        for i in var:
            if i == 1:
                D = (u"\u2680")
            elif i == 2:
                D = (u"\u2681")
            elif i == 3:
                D = (u"\u2682")
            elif i == 4:
                D = (u"\u2683")
            elif i == 5:
                D = (u"\u2684")
            elif i == 6:
                D = (u"\u2685")
            nice = nice + [D]
        return nice
        

    j = "n"
    while attempts > 0 and j == "n": #j means ready to jump
        print("attempts left: ",attempts)
        dice = roll(5)
        nice = nice_list(dice)
        print(nice)
        failed = False
        freeze = []
    
        ready = False #ready to jump
        while ready == False and failed == False:
            frozen = False #determines when the user is ready to reroll the dice 
            while frozen == False:
                take = -1
                while take < 0 or take > len(dice) - 1:
                    take = int(input("Which dice would you like to freeze? ")) - 1 #which dice the user freezes
                freeze =  freeze + [dice[take]]
                frozenice = nice_list(freeze) # makes the frozen dice pretty!!! 
                del dice[take] #removes the dice from dice and puts it in freeze
                del nice[take]
                if sum(freeze) > 8:
                    attempts = attempts - 1
                    print("You overstepped! Try again!")
                    failed = True
                    break
                if sum(freeze) == 8:
                    frozen = True
                    j = "y"
                    ready = True
                    print("you are ready to jump!")
                    break
                t = ""
                while t != "y" and t != "n":
                    t = input("Would you like to freeze another dice? y/n ")
                if t == "y":
                    frozen = False
                    if sum(freeze) > 8:
                        attempts = attempts - 1
                        print("You overstepped! Try again!")
                        failed = True
                        break
                    print("dice: ",nice)
                    print("sum of frozen dice: ",sum(freeze))
                    continue
                elif t == "n":
                    frozen = True
                if sum(freeze) > 8:
                    attempts = attempts - 1
                    print("You overstepped! Try again!")
                    failed = True
                    break
                print(nice)
                j = ""
                while j != "y" and j != "n":
                    j = input("Are you ready to jump? y/n ")
                if j == "y":
                    ready = True
                    break
                elif j == "n":
                    ready = False
                dice = roll(len(dice))
                nice = nice_list(dice)
                print("new roll: ",nice)
                frozenice = nice_list(freeze)
                print("frozen dice and sum: ",frozenice,sum(freeze))
    
    print("frozen dice: ",frozenice)
    score = 0
    dice = roll(len(freeze))
    nice = nice_list(dice)
    frozen = False
    run_up = sum(freeze) #for scoring
    run_dice = len(freeze) #for scoring
    freeze = []
    print("new roll: ",nice)
    while frozen == False and len(dice) > 0:
        take = -1
        while take < 0 or take > len(dice) - 1:
            take = int(input("Which dice would you like to freeze? ")) - 1 #which dice the user freezes
        freeze =  freeze + [dice[take]]
        frozenice = nice_list(freeze)
        del dice[take] #removes the dice from dice and puts it in freeze
        del nice[take] #same/\
        if len(dice) == 0:
            score = sum(freeze)
            break
        t = ""
        while t != "y" and t != "n":
            t = input("Would you like to freeze another dice? y/n ")
        if t == "y":
            if len(dice) == 1:
                frozen = False
                freeze = freeze + [dice[0]]
                frozenice = nice_list(freeze)
                score = sum(freeze)
                break
            frozen = False
            print("dice: ",nice)
        elif t == "n":
            dice = roll(len(dice))
            nice = nice_list(dice)
            print("new roll: ",nice)
            print("frozen dice and sum: ",frozenice,sum(freeze))
            score = sum(freeze)
            if len(dice) == 1:
                frozen = False
                freeze = freeze + [dice[0]]
                frozenice = nice_list(freeze)
                score = sum(freeze)
                break
    print("frozen dice: ",frozenice)
    print("A run-up with a total of ",run_up,"and ",run_dice,"dice, followed by a jump resulting ",score,"points.")

elif game == 2:
    print("You have chosen 110 Metre Hurtles!")
    import random

    score = 0 # record's the user's score
    dice = [0, 0, 0, 0, 0]
    rethrows = 0 # number of rethrows

    def nice_list(var):
        nice = []
        for i in var:
            if i == 1:
                D = (u"\u2680")
            elif i == 2:
                D = (u"\u2681")
            elif i == 3:
                D = (u"\u2682")
            elif i == 4:
                D = (u"\u2683")
            elif i == 5:
                D = (u"\u2684")
            elif i == 6:
                D = (u"\u2685")
            nice = nice + [D]
        return nice
    
    for i in range(6):
        # roll five dice
        for d in range(5): #0, 1, 2, 3, 4
            dice[d] = random.randint(1,6)
        # list dice with five random numbers
        score = sum(dice)
        nice = nice_list(dice)
        print(nice)
        print("current score: ",score)
        if rethrows == 5: #if they hit max rethrows, ends loop
            break
        question = input("Do you want to roll again?  y/n ")
        if question == "n":
            break  # exit the for-loop
        elif question == "y":
            rethrows = rethrows + 1
    if rethrows == 0: # turns number into string
        rethrows = "no rethrows"
    elif rethrows == 1:
        rethrows = "one rethrow"
    elif rethrows == 2:
        rethrows = "two rethrows"
    elif rethrows == 3:
        rethrows = "three rethrows"
    elif rethrows == 4:
        rethrows = "four rethrows"
    elif rethrows == 5:
        rethrows = "five rethrows"
    print("A 110 Metre Hurdles with",rethrows,"resulting in",score,"points.")








