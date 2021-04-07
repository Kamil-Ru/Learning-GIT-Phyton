# Exercise 15 (and Solution)
#   Write a program (using functions!) that asks the user for a long string containing multiple words. 
#   Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#   My name is Michele
#   Then I would see the string:

#   Michele is name My
#   shown back to me.

#   Discussion
#   Concepts for this week:
#   More string things

# Python has a lot of interesting things you can do with strings. 
# I will show a few here, but you can see many more methods that may or may not be useful at the official Python documentation about the string format.

# Remember that strings are lists.

def funtion_backwards_order(x):
  x = x.split()
  x.reverse()
  x = ' '.join(x)
  return str(x)
  
a = input('Enter long string containing multiple words: ')
print(f'Words in backwards order, method 1: {funtion_backwards_order(a)}')

