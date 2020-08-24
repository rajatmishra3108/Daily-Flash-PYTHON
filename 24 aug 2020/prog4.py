'''
Question 4 :
You and your friend go out to eat dosa, bhel, vada pav, pani puri, etc.
Your friend says he wouldn't eat / sgare anything that has price in form of odd number.
Split the bill accordingly.
Input :
How many dishes you both want to have ?
5
Start Entering prices 
11 12 13 14 15
Output :
Ammount that you'll pay : 52.0
Ammount that your friend will pay : 13.0
'''

cnt = int(input("How many dishes you both want to have ? : "))

total = list()
for i in range(cnt):
    price = int(input("Enter price one by one : "))
    total.append(price)

mycnt = 0
frndcnt = 0
for prc in total:
    if(prc % 2 == 0):
        frndcnt += prc
    else:
        mycnt += prc

print("Amount that i am supposed to pay :", mycnt + (frndcnt / 2))
print("Amount that my friend supposed to pay :", frndcnt / 2)