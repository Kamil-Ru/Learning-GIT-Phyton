#Exercise 2

#"Ask the user for a number.
#Depending on whether the number is even or odd,
#print out an appropriate message to the user.
#Hint: how does an even / odd number react differently when divided by 2?"

#Asking fo name
name = input("Hello, what is your name? ")

#Asking for a number
number = int(input('Hello ' + name + '. Please enter a number: ' ))

#Checking the number
a = number % 2

if a == 0:
 print (name + ' number ' + str(number) + ' is even.')
else:
 print (name + ' number ' + str(number) + ' is odd.')
