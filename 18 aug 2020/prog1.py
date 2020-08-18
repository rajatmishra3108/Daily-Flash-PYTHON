'''
Question :
There is a traditional function at your home, your dad has given you the list of invited guests,
but due to some mistake, some guests are mentioned twice in the list. Remove duplicate entries 
from the list and print the output as tuple.(Order can be neglected)
Input : 
guests = ["Aunt(Paternal)", "Grandpa", "Grandma", "Uncle", "Aunt(Paternal)", "Uncle(Maternal)", "Uncle(Maternal)"] 
Output :
guests = ("Aunt(Paternal)", "Grandpa", "Grandma", "Uncle", "Uncle(Maternal)")
'''
guests = ["Aunt(Paternal)", "Grandpa", "Grandma", "Uncle", "Aunt(Paternal)", "Uncle(Maternal)", "Uncle(Maternal)"] 
print(tuple(set(guests)))