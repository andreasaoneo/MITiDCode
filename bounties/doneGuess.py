import random

def play():
    randomNumber = random.randint(1,10)
    playerGuess = 0
    playerOneHistory = []
    playerTwoHistory = []
    playerOneTries = 3
    playerTwoTries = 3
    while playerOneTries >= 0 and playerTwoTries >= 0: 
        playerGuess = input("Player one, choose a number from 1 to 10 (Tries: %s): " % playerOneTries)
        while playerGuess.isdigit() == False or playerGuess in playerOneHistory:
            if playerGuess in playerOneHistory:
                playerGuess = input("That number has already been used! Try again: ")
            else:
                playerGuess = input("Not valid! Please try again: ")
        playerOneHistory.append(playerGuess)
        playerGuess = int(playerGuess)
        if playerGuess == randomNumber:
            print("Correct! Player one has won!")
            return
        elif playerGuess < randomNumber:
            print("Too low!")
        elif playerGuess > randomNumber:
            print("Too high!")
        playerOneTries -= 1

        playerGuess = input("Player two, choose a number from 1 to 10 (Tries: %s): " % playerTwoTries)
        while playerGuess.isdigit() == False or playerGuess in playerTwoHistory:
            if playerGuess in playerTwoHistory:
                playerGuess = input("That number has already been used! Try again: ")
            else:
                playerGuess = input("Not valid! Please try again: ")
        playerTwoHistory.append(playerGuess)
        playerGuess = int(playerGuess)
        if playerGuess == randomNumber:
            print("Correct! Player two has won!")
            return
        elif playerGuess < randomNumber:
            print("Too low!")
        elif playerGuess > randomNumber:
            print("Too high!")
        playerTwoTries -= 1

play()