# The program asks the user to guess for six times a randomly choosen nr. and also gives feedback.

import random   # imports the random module

guessesTaken = 0    # defines a variable called "guessesTaken" by assigning 0 to it

print('Hello! What is your name?')  # prints out the message in the parentheses
myName = input()    # defines a variable called "myName" by assigning an input to it from the user

number = random.randint(1, 20)  # chooses a random nr from 1 to 20 with the randint funct & assigns to "number" variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # prints the msg with the "myName" variable

while guessesTaken < 6:  # while loop:following repeatedly executes as long as guessesTaken variable is smaller than six
    print('Take a guess.')  # prints out the message in the parentheses
    guess = input()     # defines a variable called "guess" by assigning an input to it from the user
    guess = int(guess)  # converts "guess" variable from string into integer

    guessesTaken += 1   # adds 1 to "guessesTaken" variable

    if guess < number:  # if statement: executes when "guess" variable is less than "number" variable
        print('Your guess is too low.')    # prints out the message in the parentheses

    if guess > number:  # if statement: executes when "guess" variable is greater than "number" variable
        print('Your guess is too high.')    # prints out the message in the parentheses

    if guess == number:     # if statement: executes when "guess" variable equals "number" variable
        break      # break statement: breaks out, countinues outside the while loop

if guess == number:     # if statement: executes when "guess" variable equals "number" variable
    guessesTaken = str(guessesTaken)    # converts "guessesTaken" variable from integer into string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
    # prints out the message in the parentheses with "myName" & "guessesTaken" variables

if guess != number:     # if statement: executes when "guess" variable does not equal "number" variable
    number = str(number)    # converts "number" variable from integer into string
    print('Nope. The number I was thinking of was ' + number)   # prints out the message with "number" variable
