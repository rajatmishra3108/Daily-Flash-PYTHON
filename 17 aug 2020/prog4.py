"""
Question : Take jersey number of Suresh Raina and MS Dhoni as command line arguments,
           treat jersey number as keys, pair them with respective names in a dictionary.
           Treat names like values. Keys must be integers in dictionary
"""
import sys

s = int(sys.argv[1])
d = int(sys.argv[2])

players = dict()
players.update({s : "Suresh Raina", d : "MS Dhoni"})
print(players)