'''
Question :
You have been given a list of legendary developers and their work in 2 different lists, in order.
Paie work of developer and name of respective developer in a tuple and store it in frozen set, adn print the output
Input :
developer = ['Linus Torvalds', 'Guido Van Rossum', 'James Gosling', 'Dennis Ritchie']
work = ['Linux', 'Python', 'Java', 'C', 'Unix']
Output :
frozenset({('James Gosling', 'Java'), ('Guido Van Rossum', 'Python'), ('Linus Torvalds', 'Linux'), ('Dennis Ritchie', 'C')})
'''
developer = ['Linus Torvalds', 'Guido Van Rossum', 'James Gosling', 'Dennis Ritchie']
work = ['Linux', 'Python', 'Java', 'C', 'Unix']

res = frozenset({(developer[i], work[i]) for i in range(len(developer))})
print(res)