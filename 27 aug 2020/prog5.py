'''
Question:
Write a program to check whether the entered number is Emirp number or not
'''

def isprime(num):
    
    for i in range(2, num):
        if(num % i == 0):
            return 0

    return 1

num = int(input("Enter the number : "))
rev_num = str(num)
rev_num = int(rev_num[::-1])
if(isprime(num) and isprime(rev_num)):
    print(f"{num} is a Emirp number")
else:
    print(f"{num} isn't a Emirp number")
