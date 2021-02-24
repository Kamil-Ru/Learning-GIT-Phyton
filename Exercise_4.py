#   Exercise 4
#   
#   Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#   (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
#   For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

name = input("Hello, what is your name? ")

a = int(input('Hello ' + name + '. Please enter a number: ' ))
c = []

for elem in range(1,a + 1):
    b = a % elem
    if b == 0:
        c.append(elem)
#c.append(a)

print ('List all the divisors number ' + str(a) + ' is: ' + str(c))

d = input()