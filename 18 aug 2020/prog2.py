'''
Question : 
You have been given a list of odd numbers between 1 to 10. 
Initialize an array with square of those odd numbers 
using generator expressions
'''
l = [1, 3, 5, 7, 9]

res = (i**2 for i in l)
for i in range(len(l)):
    print(next(res), end=" ")