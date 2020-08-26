num = int(input())

even = list()
odd = list()

while num != 0:
    if(num > 0):
        for i in range(num+1):
            if(i % 2 == 0):
                even.append(i)
            else:
                odd.append(i)
    else:
        num = num * -1
        for i in range(num+1):
            i = -(i)
            if(i % 2 == 0):
                even.append(i)
            else:
                odd.append(i)

    even_sum = sum(even)
    odd_sum = sum(odd)
    even_avg = even_sum / len(even)
    odd_avg = odd_sum / len(odd)
    if(even_avg == odd_avg):
        print(even_avg)
    else:
        print(even_avg, odd_avg) if even_avg < odd_avg else print(odd_avg, even_avg)

    if(even_sum == odd_sum):
        print(even_sum)
        break
    else:
        print(even_sum, odd_sum) if even_sum < odd_sum else print(odd_sum, even_sum)
        break
else:
    print("INVALID INPUT")