n1 = int(input())
n2 = int(input())

s1 = n1**2
s2 = n2**2
c1 = n1**3
c2 = n2**3
min_num = min((s1, s2, c1, c2))
max_num = max((s1, s2, c1, c2))

rng = tuple(range(min_num, max_num + 1))
avg = sum(rng) // len(rng)

for i in range(5):
    for j in range(i + 1):
        print(avg, end=" ")
        avg += 1
    print()
