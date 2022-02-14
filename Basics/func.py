# ------------= Python function =--------------


# def add(num1, num2):
#     return num1 + num2

# ans = add(10,20)
# print(ans)


# draw square 

# import turtle
# turtle.shape('turtle')
# turtle.color('blue')
# turtle.speed(4)


# def draw_square(side_length):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.left(90)

# draw_square(200)
# turtle.exitonclick()









# import turtle
# turtle.shape('turtle')
# turtle.color('green')
# turtle.speed(7)

# def draw_square(side_length):
#     for i in range(4):
#         turtle.forward(side_length)
#         turtle.right(90)

# counter = 0
# while counter < 90:
#     draw_square(100)
#     turtle.right(4)
#     counter +=1

# turtle.exitonclick()


# import turtle
# turtle.speed(2)

# def trivuj(side_length):
#     for i in range(3):
#         turtle.forward(side_length)
#         turtle.left(120)
# trivuj(200)
# turtle.exitonclick()



# def myfun(x):
#     print('inside myfun', x)
#     x = 10
#     print('inside myfun', x)
# x = 20
# myfun(x)
# print(x)






# def myfunc(x, y = 10, z = 0):
#     print('x =',x, 'y =', y, 'z =', z)
# x = 5
# y = 6
# z = 7

# myfunc(x, y, z)
# myfunc(x, y)
# myfunc(x)




# def add(num) :
#     result = 0
#     for number in num:
#         result += number
#     return result 
# result = add([1,2, 30, 4, 5, 9])
# print(result)


# def test_fnc(li):
#     li[0] = 10

# my_list = [1, 2, 3, 4]
# print('before function call:', my_list)
# test_fnc(my_list)
# print('after function call:', my_list)


# def myfunc(li):
#     add = sum(li)
#     return add / 2

# ans = myfunc([1,2,3,4])
# print(ans)



# def myfunc(li):
#     lent = len(li)
#     count = 0
#     for elems in li:
#         count += elems
#     return count / lent

# ans = myfunc([1,2,3,4])
# print(ans)


# li = [1, 2, 3, 4]
# count = 0
# for elem in li:
#     count += elem

# print(count)





# def spam():
#     global eggs 
#     eggs = 'spam'
# eggs = 'global'
# spam()
# print(eggs)



"""
   ===========   error handling   =============
"""


# def spam(divideBy):
#     return 42 / divideBy

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(0))
# print(spam(1))





# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument')
    
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))



# @nother w4y 


# def spam(divideby):
#     return 42 / divideby

# try:
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#     print('Error: invalid argument')





# 9uss the secret number :

import random

secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 to 20')

# Ask the player to guess 6 times 

for guessTaken in range(1, 7):
    



