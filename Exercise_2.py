# Exercise 2

# Ask the user for a number.
# Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Asking fo name
name = input("Hello, what is your name? ")

# Asking for a number
number = int(input('Hello ' + name + '. Please enter a number: ' ))

# Checking the number

if number % 2 == 0:
    print (name + ' number ' + str(number) + ' is even.')
else:
    print (name + ' number ' + str(number) + ' is odd.')

# If the number is a multiple of 4, print out a different message.

if number % 4 == 0:
    print (name + ' number ' + str(number) + ' is a multiple of 4.')
else:
    print (name + ' number ' + str(number) + ' is not a multiple of 4.')

#  Ask the user for two numbers: 
# - one number to check (call it num) 
# - and one number to divide by (check). 
#  If check divides evenly into num, tell that to the user. 
#  If not, print a different appropriate message.

number_1 = int(input(name + 'Enter a frist number: ' ))
number_2 = int(input(name + 'Enter a secend number: ' ))

if number_1 % number_2 == 0:
    print (name + ' number ' + str(number_1) + ' is a multiple of ' + str(number_2) + '.')
else:
    print (name + ' number ' + str(number_1) + ' is not a multiple of ' + str(number_2) + '.')