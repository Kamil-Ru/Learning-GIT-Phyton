
# Exercise 12

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 
# For practice, write this code inside a function.

# Concepts to practice

# Lists and properties of lists
# List comprehensions (maybe)
# Functions

import random

a = [random.randint (0, 15) for i in range (20)]
print(a)

b = [a[0],a[-1]]
print(b)


# For practice, write this code inside a function.

def frist_last (x):
    b = [x[0],x[-1]]
    print(b)
    
c = [random.randint (0, 15) for i in range (20)]
print(c)
frist_last(c)


