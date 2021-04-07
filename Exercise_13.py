# Exercise 13

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. 
# Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibonnaci_number(x):

    if x == 0:
        return 0
    if x == 1:
        return 1

    else:
        c = []
        k1 = 0
        k2 = 1

        for x in range(x):
            k = k1 + k2
            k2 = k1
            k1 = k
            c.append(k)
        return c
        
while True:
    try:
        number = int(input('Enter the number of numbers in the sequence to generate:  '))
        break
    except:
        print('Enter the number!!!')
        continue
        
print(fibonnaci_number(number))

