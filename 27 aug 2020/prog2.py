'''
Question:
Write a program to print lucas number till the entered range
'''

num = int(input("Enter Range : "))

first, second = 2, 1

if num <= 0:
    print("Enter a greater number")
elif(num == 1):
    print(first)
else:
    for i in range(num):
        print(first, end = " ")
        temp = first + second
        first = second
        second = temp