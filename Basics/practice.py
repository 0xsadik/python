

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




# sort list based on how close the number is to 50:

# def myfunc(n):
#     return abs(n - 50)

# tlist = [100, 50, 65, 23, 82]
# tlist.sort(key = myfunc)
# print(tlist)




# import turtle 
# import random 

# for i in range(20):
#     x = random.randint(-200, 200)
#     y = random.randint(-200, 200)
#     turtle.setposition(x,y)
#     turtle.dot()

# # turtle.done()
# turtle.exitonclick()


# import turtle
# import random 

# turtle.penup()

# for i in range(50):
#     x = random.randint(-200, 200)
#     y = random.randint(-200, 200)
#     turtle.setposition(x,y)
#     turtle.dot()
# turtle.exitonclick()



# with color 

# import turtle
# import random


# colors = ['red','green','purple','yellow','black','orange','blue']
# turtle.penup()


# for i in range(50):
#     x = random.randint(-100, 100)
#     y = random.randint(-100, 100)
#     # set a random position 
#     turtle.setposition(x,y)
#     # set random color
#     i = random.randint(0, len(colors) - 1)
#     turtle.dot(colors[i])

# turtle.exitonclick()



# random number game 

# import random 

# number = random.randint(1, 1000)
# attempts = 0

# while True:
#     input_number = input('Guess the number (between 1 to 100)')
#     input_number = int(input_number)

#     attempts += 1
#     if input_number == number :
#         print('yes your guess is correct! ')
#         break
#     if input_number > number :
#         print('Incorrect! pelase try to guess  a smaller number.')
#     else:
#         print('Incorrect! please try to guess a larger number. ')

# print('You tried!', attempts, 'times to find the correct number.')





# import random 

# number = random.randint(1, 1000)
# attempts = 0
# low = 1
# high = 1000

# while True:
#     print('Guess the correct number (between 1 to 1000):')
#     input_number = (low + high) // 2
#     print('My guess is ', input_number)
#     attempts += 1

#     if input_number == number:
#         print('Yes! your guess is correct.')
#         break
#     if input_number > number:
#         print('Incorrect! please try to guess a smaller number. ')
#         high = input_number - 1
#     else:
#         print('Incorrect! please try to guess a larger number.')
#         low = input_number + 1

# print(f'You tried: {attempts} times to find the correct number')




# def is_prime1(n):
#     if n < 2:
#         return False
#     prime = True
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'is divisible by', x)
#             prime = False 
#     return prime 

# while True:
#     number = input('Please enter a number  (enter 0 to exit) : ')
#     number = int(number)
#     if number == 0:
#         break
#     prime = is_prime1(number)
#     if prime is True:
#         print(number, 'is a prime number.')
#     else:
#         print(number, 'is not a prime number')




# def is_prime2(n):
#     if n < 2:
#         return False
#     prime = True
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'is divisible by', x)
#             prime = False 
#             return prime
#     return prime 


# while True:
#     number = input('please enter a number (enter 0 to exit)')
#     number = int(number)
#     if number == 0:
#         break
#     prime = is_prime2(number)
#     if prime is True:
#         print(number, 'is a prime number.')
#     else:
#         print(number, 'is not a prime number.')




# turtle diya  akibuki

# import turtle
# turtle.color('lightgreen','green')

# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.left(170)
#     if abs(turtle.position()) < 1:
#         break

# turtle.end_fill()
# turtle.exitonclick()




# fibonacci 

# fib_x = 1
# fib_next = 1 

# n = input()
# n = int(n)

# if n <= 2:
#     fib_n = 1
# else:
#     i = 3
#     while i <= n:
#         i += 1
#         fib_temp = fib_x + fib_next
#         fib_x = fib_next
#         fib_next = fib_temp

#     fib_n = fib_next

# print(fib_n)



# import turtle 

# r = 120
# a = 180
# turtle.circle(r, a)
# turtle.exitonclick()



















