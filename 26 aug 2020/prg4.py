from sys import maxsize

array = [int(x) for x in input("Put elements at once, seperated by space\n").split()]

third = second = first = -maxsize

for i in array :

    if i > first :
        third = second
        second = first
        first = i

    elif i > second :
        third = second
        second = i

    elif i > third :
        third = i

print(third)
