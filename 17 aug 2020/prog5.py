"""
Question : Write a Python program which accepts your name, 
           like("Rajat Mishra") and print output as 
           My--name--is--Rajat--Mishra.
"""
name = input("Enter Your Name : ")
output = "--".join(f"My name is {name}".split())
print(output)
