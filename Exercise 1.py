# Exercise 1

#"Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old."

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


print ('In ' + age_100 + ', you will be 100 years old.')
