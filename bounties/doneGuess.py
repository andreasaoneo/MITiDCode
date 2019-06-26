from random import randint

def play():
    answer = randint(1,10)
    guess = 0
    onehistory = []
    twohistory = []
    onetries = 3
    twotries = 3
    while onetries >= 0 and twotries >= 0:

        guess = input("Player one, choose a number from 1 to 10 (Tries: %s): " % onetries)
        while guess.isdigit() == False or guess in onehistory:
            if guess in onehistory:
                guess = input("That number has already been used! Try again: ")
            else:
                guess = input("Not valid! Please try again: ")
        onehistory.append(guess)
        guess = int(guess)
        if guess == answer:
            print("Correct! Player one has won!")
            return
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        onetries -= 1

        guess = input("Player two, choose a number from 1 to 10 (Tries: %s): " % twotries)
        while guess.isdigit() == False or guess in twohistory:
            if guess in twohistory:
                guess = input("That number has already been used! Try again: ")
            else:
                guess = input("Not valid! Please try again: ")
        twohistory.append(guess)
        guess = int(guess)
        if guess == answer:
            print("Correct! Player two has won!")
            return
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        twotries -= 1

play()