from time import clock

start = clock()

history = {'French Revolution' : 1789, 'Industrial Revolution' : 1760, "Greek Revolution" : 1821, "Serbian Revolution" : 1748}

n1 = input("Enter first event\n")
n2 = input("Enter second event\n")

for i in history :

    if n1 == i:
        year1 = history[i]

    elif n2 == i:
        year2 = history[i]

print(abs(year1-year2))
end = clock()
print(end - start)
