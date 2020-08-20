'''
Write a function such that it accepts keyword arguments
while being called.
Create a dictionary with those keyword arguments inside
the function.
'''
def fun(**dc):
    print(dc)

fun(Dhoni = 7, Virat = 18, Raina = 3, Rohit = 45)