#   
#   Exercise 5
#   
#   Take two lists, say for example these two:
#   
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#   
#   and write a program that returns a list that contains only the elements that are common between the lists
#   (without duplicates). Make sure your program works on two lists of different sizes.
#   
#   Extras:
#   1. Randomly generate two lists to test this
#   2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
#   

a = [1, 1, 2, 3, 5, 8, 0, 21, 34, 55, 89, 100, 50, 200, 13, 13, 13, 125, 1000]
b = [1000, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 125]
c = []

for x in a:
    if x in b:
        if x not in c:
            c.append(x)

print('Answer for exercise 5 = '+ str(c))

a.clear()
b.clear()
c.clear()

#   Extras 1

import random

a = [random.randint(0,15) for i in range(18)]
b = [random.randint(0,15) for i in range(10)]

print('Random list a: ' + str(a))
print('Random list b: ' + str(b))

#   Extras 2

#for x in a and b if x in a and b
#    c.append(x)
c = list(set(a) & set(b))
c.sort()
print('Common between the lists a and b (without duplicatesc): ' + str(c))
