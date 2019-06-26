#Imports
import math
import random
import nltk
from nltk.corpus import words


# Variables
word = words.words()[random.randint(1,236736)]
global hidden
hidden = []
global letters
letters = []
history = []


# Functions

def isInList(l,e):
    for i in l:
        if(i == e):
            return True
    return False

def init(w):
    for i in w:
        hidden.append(' _')
    for j in range(len(w)):
        letters.append(w[j])

def returnListAsString(h):
    returnString = ""
    for i in range(len(h)):
        returnString += h[i]
    return returnString

def getGuess():
    guess = input("Take a guess! ")
    # if guess == "stop":
    #     return "stop"
    while guess.isalpha() == False or len(guess) > 1 or guess in history:
        if guess in history:
            guess = input("You've used that letter before! Try a different one: ")
        else:
            guess = input("You can only enter one letter! ")
    
    history.append(guess.lower())
    history.append(guess.upper())
    return guess.lower()


def checkGuess(g, t):
    if isInList(letters,g):
        for i in range(len(letters)):
            if returnListAsString(letters)[i] == g:
                hidden[i] = letters[i]
        return ["You guessed correctly! ", t]
    else:
        t -= 1
        return ["That letter isn't in the word!", t]




# Debugging



# Main Execution

tries = math.ceil(len(word)/1.4)
if tries > 20:
    tries = 18

print("Welcome to hangman!")

init(word)

print(returnListAsString(hidden))

while not hidden == letters and tries > 0:
    #if getGuess() == "stop":
        #exit(0)
    print("You have "+ str(tries) + " tries remaining!")
    res = checkGuess(getGuess(), tries)
    print(res[0])
    tries = res[1]
    print(returnListAsString(hidden))
    


if tries <= 0:
    print("You lost! " + word)
else:
    print("You win!")