"""
Question : Use list to take and store integer values from user 
           and unpack it.
           Justify the reason for too many values to unpack
           Justify the reason for not enough values to unpack
"""
l = [int(i) for i in input("Enter values on same line : ").split()]

print("Values in the list : ")
for val in l:
  print(val, end=" ")

"""
Suppose user entered five elements
val1, val2, val3, val4, val5 = l
print(val1)
print(val2)
print(val3)
print(val4)
print(val5)
Then it has five variables to store vlaues from list
"""

"""
But if we give 6 variables to unpack 5 values
val1, val2, val3, val4, val5, val6 = l

It will raise a error 
ValueError : Too many values to unpack
"""

"""
But if we give 3 variables to unpack 5 values
val1, val2, val3 = l

It will raise a error 
ValueError : Not Enough values to unpack
"""