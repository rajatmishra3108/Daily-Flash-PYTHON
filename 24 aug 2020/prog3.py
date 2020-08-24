'''
Question :
Write a program to check whether two entered strings are anagram strings
'''
def isanagram(str1, str2):

    if(len(str1) != len(str2)):
        return 0
    else:
        if(sorted(str1) == sorted(str2)):
            return 1
        return 0

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

if(isanagram(str1, str2)):
    print("The enetered two strings are panagram of each other")
else:
    print("The enetered two strings aren't panagram of each other")
