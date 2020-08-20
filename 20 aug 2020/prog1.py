'''
Question :
You have been given a list of tuples, where each nested tuple
consits of name of batsman, and his dominant batting hand.
Create a dictionary such that name of batsman is acting as
key, and his batting hand is the value.
Output :
{'Dhoni':'Right', 'Raina':'Left', 'Jadeja':'Left', 'Rohit':'Right'}
'''
player_hand = (('Dhoni', 'Right'), ('Raina', 'Left'), ('Jadeja', 'Left'), ('Rohit', 'Right'))
print(dict(player_hand))