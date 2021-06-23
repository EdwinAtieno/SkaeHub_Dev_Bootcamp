# This is a guess the number game.

# Import random library
import random

# instantiate guessestaken = 0
guessesTaken = 0



print('Hello! What is your name?\n')

myName = input()

number = random.randint(1, 10)

print('Therefore, ' + myName + ', I am thinking of a number between 1 and 10. Guess my number')


# checks the number of times of guess taken
while guessesTaken < 6:

    print('Take a guess\n\t.')

    guess = int(input())

    # add 1 after every guess
    guessesTaken = guessesTaken + 1

    #checking the conditions
    if guess < number:

        print('Your guess is too low.')



    if guess > number:

        print('Your guess is too high.')



    if guess == number:
        break

# If user gets answer after first guess
if guess == number:

    guessesTaken = str(guessesTaken)

    print('Great, ' + myName + '! your passed number in ' + guessesTaken + ' guesses!')

# if user guess wrong answers
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)