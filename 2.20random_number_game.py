# while-else
# Simple guessing game: start with a random number and
# guess with hints until:
#	guess is correct
#	the guess is out of range indicating the user is quitting
# All non-typed variables are integers : Rule 4

import random # get the random number module
number = random.randint(0,100) # grab a random number from module
			       # between 0 and 100 inclusive
print("Hi-Lo Number Guessing Game: between 0 and 100 inclusive.")
print ()

# get an initial guess
guess_str = input("Guess a number: ")
guess = int(guess_str) #convert the string into an integer

# while guess is in range, keep asking.
while 0 <= guess <= 100:
    if guess > number:
        print("Guessed too high.")
    elif guess < number:
        print("Guessed too low.")
    else:
        print("You guessed it. The number was:",number)
        break
    # keep going, get the next guess
    guess_str = input("Guess a number: ")
    guess = int(guess_str)
else:
    print("You quit early, the number was:",number)
    
