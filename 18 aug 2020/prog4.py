'''
Question :
You have given a dictionary of players, with their name as key and their team as value.
Sort the players in the list of their respective teams
Input :
auction = {'Watson' : 'CSK', 'Raina' : 'CSK', 'Dhoni' : 'CSK', 'Rohit' : 'MI', 'Malinga' : 'MI', 'Pandya' : 'MI'}
Output : 
CSK = ['Watson', 'Raina', 'Dhoni']
MI = ['Rohit', 'Malinga', 'Pandya']
'''
auction = {'Watson' : 'CSK', 'Raina' : 'CSK', 'Dhoni' : 'CSK', 'Rohit' : 'MI', 'Malinga' : 'MI', 'Pandya' : 'MI'}

CSK = [key for key, val in auction.items() if val == 'CSK']
MI = [key for key, val in auction.items() if val == 'MI']

print(CSK)
print(MI)