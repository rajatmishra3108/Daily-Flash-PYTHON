def gcd(n1, n2) :

    small = int(min(n1, n2))

    for i in range(small, 0, -1) :

        if n1 % i == 0 and n2 % i == 0:
            return i

def lcm(n1, n2) :

    result = n1 * n2 / gcd(n1, n2)
    return result

ls = [int(x) for x in input("Enter list\n").split()]

found = ls[0]

for i in range(1, len(ls)) :

    found = lcm(found, ls[i])

print(found)
