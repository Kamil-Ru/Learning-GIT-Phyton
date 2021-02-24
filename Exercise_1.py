# Exercise 1

#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Importing the date
import datetime

#Asking fo name
name = input("Hello, what is your name? ")
print ("Hello " + name)

#Asking for a age
age = input('How old you are ' + name + '? ')

now = datetime.datetime.now()
now_2 = now.year

age_100 = str(now_2 + 100 - int(age))

msg = 'In ' + age_100 + ', you will be 100 years old.'
print (msg)


# Extras 1 
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)

# Extras 2
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

number = int(input('Pleas ' + name + ', enter a number: '))

print('Extras 1: ')

# Alternative

# for x in range(number):
#  print ('In ' + age_100 + ', you will be 100 years old.')

print ((msg + '\n' ) * number)