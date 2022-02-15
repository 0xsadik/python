
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


# spam = [1, 3, 2, 'a', 'c','b']
# spam.sort()
# print(spam)


# spam = ['c','b','a']
# spam.sort()
# print(spam)




# magic 8 ball with a list 


# import  random

# messages = ['It is certain','It is decidely so','Yes definitely',
# 'Reply hazy try again','ask again later','concenatrate and ask again','my reply is no'
# ,'Outlook not so good','Very doubtful']

# print(messages[random.randint(0, len(messages) - 1)])


# list copying...
# copy() 

# tlist = ['apple','banana','cherry']
# mlist = tlist.copy()
# print(mlist)



# make a copy of a list wit the list() method:

# tlist = ['apple','banana','cherry']
# mlist = list(tlist)
# print(mlist)



"""

            Python - Join Lists

"""



# join two lists

# list1 = ['a','b','c']
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)



# another way


# list1 = ['a','b','c']
# list2 = [1, 2, 3]

# for x in list2:
#     list1.append(x)

# print(list1)


# extend()



list1 = ['a','b','c']
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)





