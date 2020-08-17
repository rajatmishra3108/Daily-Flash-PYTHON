"""
Question : Write a program such that if "68 72 79 78 73" given as
           command line argument, "DHONI" should be the output
"""
import sys

d = int(sys.argv[1]) 
h = int(sys.argv[2]) 
o = int(sys.argv[3]) 
n = int(sys.argv[4]) 
i = int(sys.argv[5]) 

print(chr(d) + chr(h) + chr(o) + chr(n) + chr(i))