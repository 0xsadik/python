"""
    =========== Sets ============
"""


# set are used to store multiple items in a sing le variable 

# a set is a collection which is unordered, unchangeable and unindexed


# set

# tset = {'apple','banana','cherry'}
# print(tset)



# duplicates not allowed 

# tset = {'apple','banana','pineapple','apple'}
# print(tset)


# len() 
# tset = {'apple','banana','pineapple','apple'}
# length = len(tset)
# print(length)



# a set with strings, integers and boolean values:

# set1 = {'abc', 34, True, 40, 'male'}
# print(set1)


# check type 

# set1 = {'abc', 34, True, 40, 'male'}
# print(type(set1))


# the set() constructor 

# using set() constructor to make a set 

# tset = set(('apple','banana','pineapple','mango'))
# print(tset)



# pythone - Access set items 

# tset = {"apple", "banana", "cherry"}

# for x in tset:
#     print(x)


# check if banana is present in the set

# tset = {"apple", "banana", "cherry"}
# print('banana' in tset)



# Python - Add Set Items


# tset = {"apple", "banana", "cherry"}
# tset.add('orange')
# print(tset)




# add sets
# to add items from another set into the current set, use the 'update()' method 


# tset = {"apple", "banana", "cherry"}
# tset2 = {'pineapple','mango','papaya'}

# tset.update(tset2)
# print(tset)




# ============ Remove set items ===============


# to do so use: remove() , discard()

# tset = {'apple','banana','cherry'}
# tset.remove('banana')
# print(tset)


# tset = {'apple','banana','cherry'}
# tset.discard('apple')
# print(tset)


# pop() method 

# tset = {'apple','banana','cherry'}
# x = tset.pop()
# print(x)
# print(tset)


# clear() method 

# tset = {'apple','banana','cherry'}
# tset.clear()
# print(tset)


# ----- loop set --------

# tset = {'apple','banana','cherry'}
# for a in tset:
#     print(a)


# ---------- join sets -----------


# join two sets

# set1 = {'a','b','c'}
# set2 = {1, 3, 2}
# set3 = set1.union(set2)
# print(set3)



# set1 = {'a','b','c'}
# set2 = {1, 2, 3}

# set1.update(set2)
# print(set1)


# keep only the # duplicates #

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)



# return a set that contains the items that exist in both set x, and set y :

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)



# keep all but not the Duplicates:

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)


# return a set that contains all items for both sets, except items that are present in both

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)



""" ======== set methods ======== """

# add()
# clear()
# copy()
# difference()
# difference_update()
# discard() 
# intersection()
# intersection_upate()
# isdisjoint()
# issubset()
# pop()
# remove()
# symmetric_difference()
# symmetric_difference_update()
# union()
# update()










































