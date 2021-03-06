
#   Exercise 9

#   Generate a random number between 1 and 9 (including 1 and 9). 
#   Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
#   (Hint: remember to use the user input lessons from the very first exercise)

#     Extras:

#     -   Keep the game going until the user types “exit”
#     -   Keep track of how many guesses the user has taken, and when the game ends, print this out.

#     Discussion

#   Concepts for this week:

#     -   Modules
#     -   Random numbers
#     -   User input

import random

def game ():
    x = random.randint(1, 9)
    count = 0
    while True:
          y = int(input('Pleas input number\n\n\n'))
          if x == y: 
              print('!!!EXACTLY RIGHT !!!\nGuesses the user has taken: ' + str(count))
              break
          elif x < y: 
              count += 1
              print('Your number is too high\n\n\n')
          elif x > y: 
              print('Your number is too low\n\n\n')
              count += 1

while True:
    menu = input(print('MENU \nPleas type:\n1. New game\n2. Exit\n'))
    if menu == '1':
        game()
    elif menu == '2':
        break