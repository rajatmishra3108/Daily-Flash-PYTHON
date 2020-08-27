'''
Question:
Write a program to generate random number within a specific range
'''

from random import randint

rng = int(input("Enter Range : "))
print(randint(0, rng))