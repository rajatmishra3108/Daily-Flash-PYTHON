'''
Question :
You have been given a dictionary of movie(key) and cat(value)
collection = {"The Last samurai":"Tom Cruise, Ken", "Justice League":"Cavil, Gadot", "MI":"Tom Cruise"}
Print a list of movies, where cruise is not a part of cast.
Output:
['Justice League']
'''
collection = {"The Last samurai":"Tom Cruise, Ken", "Justice League":"Cavil, Gadot", "MI":"Tom Cruise"}

res = [movie for movie in collection.keys() if('Cruise' not in collection[movie])]
print(res)
