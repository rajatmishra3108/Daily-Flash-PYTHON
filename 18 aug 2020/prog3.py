'''
Question : 
You have been given a list.
cricketers = ['Kapil', 'Kohli', 'Raina', 'Chahal', 'Dhoni', 'Pant', 'Dravid', 'Bumrah', 'Harbhajan']
Iterate over the list in reverse order, such that only retired players name should be printed.
(Players retired from international cricket)
'''
cricketers = ['Kapil', 'Kohli', 'Raina', 'Chahal', 'Dhoni', 'Pant', 'Dravid', 'Bumrah', 'Harbhajan']

retired = [cricketers[i] for i in range(len(cricketers)) if i % 2 == 0]
print(retired)