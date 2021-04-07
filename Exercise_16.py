# Exercise 16 (and Solution)

# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
# Discussion
# There are no new topics this week, but you will need to use Python’s random module, described in this post.
'''
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols

For weak passwords, pick a word or two from a list'''

import random
import string

class Password:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def weak(self):

        base = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Zero']
        return ' '.join(random.choice(base) for i in range (self.numbers))
        
    def strong(self):
        
        base = string.ascii_letters + string.digits	+ string.punctuation
        return ''.join(random.choice(base) for i in range (self.numbers))
        

def password_long():
    while True:
        try:
            return int(input('How long should be password? Type a number: '))
        except:
            continue    
        
while True:
    
        user_decision = input("How STRONG should be password? Type:\n   '1' for WEAK passwords\n   '2' for STRONG passwords\n ")
        if user_decision == '1':
            password_long = password_long()
            Password = Password(password_long)
            print(Password.weak())
            break

        elif user_decision == '2':
            password_long = password_long()
            Password = Password(password_long)
            print(Password.strong())
            break

    
       
    



    
