
# automate boring list 


# frnds = ['shakil','babu','fahim','morshed','torikus','sadik']
# # fmt = frnds[2:5]
# startToEnd = frnds[0:4]
# print(startToEnd)


# removing values from lists with del statements

# spam = ['shakil','babu','fahim','morshed','torikus','sadik']
# del spam[5]
# print(spam)


# -> working with lists 

# print('Enter the name of cat 1: ')
# catname1 = input()
# print('Enter the name of cat 2: ')
# catname2 = input()
# print('Enter the name of cat 3: ')
# catname3 = input()
# print('Enter the name of cat 4: ')
# catname4 = input()
# print('Enter the name of cat 5: ')
# catname5 = input()

# print(catname1 + ' ' + catname2 + ' ' + catname3 + ' ' + catname4 + ' ' + catname5)




# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop.): ')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name] 
# print('The cat names are:')
# for name in catNames:
#     print('  ' + name)





# names = ['shakil','babu','fahim','morshed','torikus','sadik']
# for i in names:
#     print('One of my friend is : ',i)




# the 'in' and 'not' operator 


# names = ['torikus','sadik','raihan']
# print('sadik' in names)
# print('torikuss' not in names)




# myPets = ['zophie','pooka','toka']
# print('enter a pet name:')
# name = input()
# if name not in myPets:
#     print('I do not have a pet named' + name)
# else:
#     print(name + 'is my pet.')




# the multiple assignment trick


# cat = ['fat','black','loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]

# size, color, dispostion = cat


# print(cat)




# --> append()

# spam = ['cat','dog','bat']
# spam.append('moose') # will add to the last of this list 
# print(spam)



# --> insert()

# spam = ['babu','fahim','morshed']
# spam.insert(0, 'shakil')
# print(spam)




# --> remove()

# spam = ['cat','bat','rat','elephant']
# spam.remove('bat')
# print(spam)



# --> sort()

# spam = [2, 4, 6, 3, 5, 8, 9]
# spam.sort()
# print(spam)






