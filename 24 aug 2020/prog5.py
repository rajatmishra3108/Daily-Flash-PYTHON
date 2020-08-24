'''
Question :
You have given a dictionary of food items in a wedding,
Your friend belongs to a orthodox family, he says that
if weekday is odd then only he'll eat veg and non-veg both
otherwise only veg.
Find out how many dishes your fried can eat depending on weekday number
'''
meals = {'Paneer':'Veg', 
         'Mutton Korma':'Non-Veg',
         'Chicken Malai':'Non-Veg',
         'Tandoori Roti':'Veg',
         'Drumsticks':'Non-Veg'}

week_day = int(input("Hey, what number of weekday it is ? : "))

vegcnt = 0
nonvegcnt = 0
for val in meals.values():
    if(val == 'Veg'):
        vegcnt += 1
    else:
        nonvegcnt += 1

if(week_day % 2 == 0):
    print(f"My friend can eat {vegcnt} dishes")
else:
    print(f"My friend can eat {vegcnt + nonvegcnt} dishes")
