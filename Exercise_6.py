#   
#   Exercise 6
#   
#   Ask the user for a string and print out whether this string is a palindrome or not. 
#   (A palindrome is a string that reads the same forwards and backwards.)
#   


name = input('Hello, whats is your name?\n')
string = input('Please ' + name + ' enter any worlds: ')
string_array = []

string = string.lower()

for x in string:
    if x == ' ': continue
    else:
        string_array.append(x)

k = 0
h = len(string_array)

print(len(string_array))

for x in string_array:
    if string.lower[x] == string.lower[-x]:
        print(OK)



print(string_array)
print(string)