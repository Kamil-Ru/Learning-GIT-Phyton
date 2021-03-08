# Exercise 11 (and Solution)
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

# Discussion
# Concepts for this week:

# Functions
# Reusable functions
# Default arguments

# Exercise 4 + 11

name = input("Hello, what is your name? ")

def get_integr(help_text = name + ' give me a number: '):
    return int(input(help_text))

a = get_integr()
c = []

for elem in range(1,a + 1):
    b = a % elem
    if b == 0:
        c.append(elem)

print ('List all the divisors number ' + str(a) + ' is: ' + str(c))


# Exercise 2 + 11 (For practice)

number_1 = get_integr('Enter frist nuber: ')
number_2 = get_integr('Enter secend nuber: ')

c = number_1 % number_2

if c == 0:
    print (name + ' number ' + str(number_1) + ' is a multiple of ' + str(number_2) + '.')
else:
    print (name + ' number ' + str(number_1) + ' is not a multiple of ' + str(number_2) + '.')

