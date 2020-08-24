'''
Question :
Write a program to illustrate the logic of 'Strcmp' function of C 
'''
def strcmp(str1, str2):

    for char in range(len(str1)):
        if(str1[char] < str2[char]):
            print(f"strcmp(str1, str2) = {ord(str1[char]) - ord(str2[char])}")
            break
        elif(str1[char] > str2[char]):
            print(f"strcmp(str1, str2) = {ord(str1[char]) - ord(str2[char])}")
            break
    else:
        print(f"strcmp(str1, str2) = {0}")

strcmp("abCd", "abcd")