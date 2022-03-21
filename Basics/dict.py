# ================= python dictionaries =======================


# Dictionary

# dictionary = {
#     "name" : "torikus",
#     "age" : 24,
#     "country" : "Bangladesh",
#     "year" : 2022
# }
# print(dictionary)



# Dictionary items 

# tdic = {
#     'brand' : 'Ford',
#     'model' : 'mustang',
#     'year' : 1723
# }
# print(tdic['year'])


# duplicate not allowed

# tdic = {
#     'brand' : 'Ford',
#     'model' : 'mustang',
#     'year' : 2022,
# }
# print(tdic)


# dictionary items  - Data types 


# tdic = {
#     'brand' : 'Ford',
#     'electric' : False,
#     'year' : 1964,
#     'colors' : ['red','white','blue']
# }
# print(tdic)
# print(type(tdic))



# ---> Access dictionary items 


# tdic = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# temp = tdic['model']
# print(temp)


# get() method does the same thing 

# tdic = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# temp = tdic.get('year')
# print(temp)






# --->  get keys 



# tdic = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# temp = tdic.keys()
# print(temp)




# add a new item to the original dictionary and see that the keys list gets updated


# car = {
#     'brand' : 'Ford',
#     'model' : 'Mustang',
#     'year' : 1996
# }

# temp = car.keys()
# # print(temp)

# car['color'] = 'White'
# print(car)


# GET values 


# tdic = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# temp = tdic.values()
# print(temp)




# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change


# add a new item to the orginal dictionary, and see that the values list gets updated as well:


# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x)
# car['color'] = 'red'
# print(x)


# --> Get items 

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# temp = car.items()
# print(temp)


# marks = [77, 76, 65, 78, 62, 64, 60, 77, 78, 89, 98, 45, 33]
# roll = input('please enter your roll here:')
# roll = int(roll)
# print(f'You have got: {marks[roll] } marks. ')


# tdict = {'shakil' : 23, 'tori': 22, 'fahim' : 23}
# sh = tdict['shakil']
# print(sh)






# ---> --------- > ---------------> ---------------------> 








# copy a Dictionary 


# copy() method 


# thisdict = {
#     'brand' :'Ford',
#     'model' : 'Mustang',
#     'year' : 1994
# }

# mydict = thisdict.copy()
# print(mydict)



# -> another way


# thisdict = {
#     'brand' :'Ford',
#     'model' : 'Mustang',
#     'year' : 1994
# }

# mydict = dict(thisdict)
# print(mydict)


# --< Nested Dictionaries 

myfam = {
    'child1' : {
        'name' : 'Emil',
        'year' : 2003
    },
    'child2': {
        'name ' : 'Tobias',
        'year' : 2005
    },
    'child3' : {
        'name' : 'Linux',
        'year' : 2008
    }
}

print(myfam)


# -> Dictionary methods 

# clear() ---       removes all the elements from the dictionary
# copy()  ---       returns a copy of the dictionary 
# formkey() ---     returns a dictionary with the specified keys and value
# get()     ---     returns the value of the specific key
# items() ---       returns a list containing a tuple for each key value pair
# keys() ---        returns a list containing the dictionary's keys
# pop() ---         removes the last inserted key-value pair 
# popitem() ---     removes the last inserted key value pair 
# setderfault() --- returns the value of the specified key. If the key does not exist : insert the key , with the specified value 
# update() ---      updates the dictionary with the specified key-value pairs
# values() ---      returns a list of all the values in the dictionary
 

 













































