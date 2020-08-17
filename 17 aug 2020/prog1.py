"""
Question : Use list to take and store INTEGER values from user 
           not STRING, in one variable
"""
l = [int(i) for i in input("Enter values on same line : ").split()]
print(l)
