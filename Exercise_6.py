#   
#   Exercise 6
#   
#   Ask the user for a string and print out whether this string is a palindrome or not. 
#   (A palindrome is a string that reads the same forwards and backwards.)
#   
name = input('Hello, whats is your name?\n')
string = input('Please ' + name + ' write any word: ')
string_array = []

string = string.lower()

for x in string:
    if x in [' ', ',', '.']: continue
    else:
        string_array.append(x)
       
if string_array == string_array[::-1]:
    print('The word is a palindrome !!!')
else:
    print('The word is NOT a palindrome !!!')