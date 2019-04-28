# Debugging Coin Toss
# The following program is meant to be a simple coin toss guessing game. 
# The player gets two guesses (it’s an easy game). 
# However, the program has several bugs in it. Run through the program 
# a few times to find the bugs that keep the program from working correctly.

import random, logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
# toss = random.randint(0, 1) # 0 is tails, 1 is heads
toss = random.randint(0, 1) # 1st error: toss should be change to integer to match userinput
if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # guesss = input()   
    guess = input() #2nd error: spelling mistake
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')