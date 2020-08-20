'''
Question :
You have been given a dictionary.
dc = {'Germany':'Berlin', 'Italy':'Venice', 'France':'Versailles', 'Canada':'Quebec City'}
iterate dictionary such that, keys and values are printed alternatively.
Output : 
Germany
Venice
France
Quebec City
'''
dc = {'Germany':'Berlin', 'Italy':'Venice', 'France':'Versailles', 'Canada':'Quebec City'}
for key in dc.keys():
    print(dc[key]) if(key == 'Canada') else print(key)