import random

def isInList(i,l,e):
    for i in l: 
        if(i == e):
            return True
    return False


def getInput(t):
    i = input('Guess a number (1-10): ')
    if t % 2 == 0:
        if isInList(i,playerTwoHistory,i):
            i = input('You have already made that guess')
    else:
        if isInList():
            i = input('You have already made that guess')

while True:
    playerOneGuess = -6.66
    playerTwoGuess = -6.66
    playerOneHistory = []
    playerTwoHistory = []
    turn = 10

    # while turn > 0:
