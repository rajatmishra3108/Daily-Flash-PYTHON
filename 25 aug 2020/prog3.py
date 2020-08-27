friends = [str(x) for x in input("Enter name of all friends\n").split()]

count = 0

for name in friends :

    i = 0
    j = len(name) - 1
    flag = 0

    while(i < j) :

        if name[i] != name[j]:
            flag = 1
            break

        i += 1
        j -= 1

    if flag == 0 :
        count += 1

print(count, 'friends will get the discount')
