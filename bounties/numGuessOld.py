import random

def getInput(o, t, w):
    i = input("Guess the Number (1 to 10):")
    try:
        int(i)
    except ValueError:
        i = input("Please enter a number: ")

    if i == o:
        i = input("Don't guess the same thing: ")
    elif i > selectedNum:
        o = i
        i = input("Too high! Try again: ")
        t -= 1
    elif i < selectedNum:
        o = i
        i = input("Too low! Try again: ")
        t -= 1
    elif i == selectedNum:
        w = True
    return o, t, w, i


while True:
    selectedNum = random.randint(2, 11)
    print(selectedNum)
    oldGuess = -666
    tries = 5
    won = False
    returns = getInput(oldGuess, tries, won)
    oldGuess = returns[0]
    tries = returns[1]
    won = returns[2]
    guessedNum = returns[3]
    while tries > 0:
        print("You have %s tries left"%(tries))

        returns = getInput(oldGuess, tries, won)
        oldGuess = returns[0]
        tries = returns[1]
        won = returns[2]
        guessedNum = returns[3]

    if won and input("It is "+str(selectedNum)+"! Congratulations! Play again? [yes/no]") == "yes":
        continue
    elif not won and input("The number was "+str(selectedNum)+".. Play again? [yes/no]") == "yes":
        continue

    else:
        exit(0)

