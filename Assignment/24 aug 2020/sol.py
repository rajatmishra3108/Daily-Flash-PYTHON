start = int(input())
end = int(input())

if(start == end):
    print("INVALID RANGE")
else:
    even_sum = 0
    odd_sum = 0
    even = list()
    odd = list()
    for i in range(start, end + 1):
        if(i % 2 == 0):
            even_sum += i 
            even.append(i)
        else:
            odd_sum += i    
            odd.append(i)
    if(sum(even) > sum(odd)):
        for i in range(len(even)):
            if((i+1) % 5 == 0):
                print(even[i])
            else:
                print(even[i], end=" ")
    else:
        for i in range(len(odd)):
            if((i+1) % 5 == 0):
                print(odd[i])
            else:
                print(odd[i], end=" ")