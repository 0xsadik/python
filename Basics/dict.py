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

































