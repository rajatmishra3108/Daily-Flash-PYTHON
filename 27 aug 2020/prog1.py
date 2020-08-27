'''
Question:
Write a program to find whether the number is narcisstic or not
'''

num = int(input("Enter a number : "))
power = len(",".join(str(num).split()))

addition = 0
temp = num
while temp != 0:
    rem = temp % 10
    addition += rem ** power
    temp = temp // 10

if(addition == num):
    print(f"{num} is a Narcisstic number")
else:
    print(f"{num} is a not a Narcisstic number")
