#   Exercise 14
#   Write a program (function!) that takes a list and returns a new list 
#   that contains all the elements of the first list minus all the duplicates.

#   Extras:

#       -   Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#       -   Go back and do Exercise 5 using sets, and write the solution for that in a different function.

#   Discussion
#   Concepts for this week:
#   Sets


#   Sets
#   In mathematics, a set is a collection of elements where no element is repeated. 
#   This becomes useful because if you know your data is stored in a set, you are guaranteed to have unique elements.


a = [1, 1, 1, 2, 2, 2, 5, 5, 10, 11, 10]


# for i in c:
#     k = 0
#     while k == len(a):
#         if c[i] == c[i+k]:
#             c.remove(c[i])
#     k += 1

def function_list(x):
    
    y = []
    
    for i in x:
        
        if i in y:
            continue
                        
        else:
            y.append(i)
    
    return y
        
    
c = function_list(a)
    
b = list(set(a))

print(f'List: {a}')

print('Using sets: ' + str(b))

print(f'Using funtion: {c}')
