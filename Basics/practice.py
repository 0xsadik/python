

# loop exersise

# import turtle

# turtle.shape('turtle')
# turtle.color('green')

# def first(f_length):
#     for f in range(2):
#         turtle.forward(f_length)
#         turtle.left(90)
#         turtle.forward(100)
#         turtle.left(90)
#     turtle.penup()
#     turtle.forward(60)
#     turtle.left(90)
#     turtle.forward(55)
#     turtle.right(140)


# def second(s_length):
#     for s in range(2):
#         turtle.pendown()
#         turtle.forward(s_length)
#         turtle.left(90)
#         turtle.forward(s_length)
#         turtle.left(90)
#     turtle.penup()
#     turtle.left(90)
#     turtle.forward(250)

# first(200)
# second(55)
# turtle.exitonclick()


# a = 'apple'
# b = 'apple'
# c = a is b
# print(c)
# True


# a = 'tsr'
# b = 'tsr'
# print(a is b)
# #True


# a = 'trs!'
# b = 'trs!'
# print(a is b)
# # output???


# a = 256
# b = 256
# print(a is b)

# a = 300
# b = 300
# print(type(a))
# print(type(b))
# print(a is b)


# a =  input('enter a number herE:')
# print(type(a)) #string
# print('the numebr is:', a)


# a = 'asdf'
# b = 'asdf'
# print(a is b)

# a = 256
# b = 256
# print(a is b)

# a = 300
# b = 300
# print(a is b)


# a = 115
# b = 115
# print(a is b)


# list1 = ['torikus','shakil','fahim']
# print(id(list1[0]))
# print(id(list1[1]))
# print(id(list1[2]))


# def binn(num):
#     result = bin(num)
#     print(result)
# binn(19)



# tlist = ['apple', 'banana','cherry']
# tlist.pop()
# print(tlist)


# -> del

# tlist = ['apple','banana','cherry']
# del tlist[1]
# print(tlist)



# -> delete entire list 

# tlist = ['apple','banana','cherry']
# del tlist
# print(tlist)


# ll1 = ['apple','banana','cherry','bery']
# for i in range(len(ll1)):
#     print(f'index is : {i} and element is : {ll1[i]}')



# -> using while loop

# tlist = ['apple','banana','cherry']
# i = 0
# while i < len(tlist):
#     print(tlist[i])
#     i = i + 1



# tlist = ['apple','banna','cherry']
# [print(x) for x in tlist]



"""

    python list comprehension

"""


# fruits = ['apple','banana','cherry','kiwi','mango']
# newlist = []

# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)

# print(newlist)



# furits = ['apple','banana','cherry','kiwi','mango']
# newlist = [ x for x in furits if 'a' in x]
# print(newlist)


# only accept items that are not 'apple'

# frt  = ['apple','banana','pineapple']
# newlist = [x for x in frt if x != 'apple']
# print(newlist)


# frt  = ['apple','banana','pineapple']
# newlist =  [x for x in  frt]
# print(newlist)


# arr = [10, 3, 4, 8, 9, 2, 1]
# arr.sort()
# arr.sort(reverse=True)
# print(arr)




