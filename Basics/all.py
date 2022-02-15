
# =-= if statement =-=


# saarc = ['bangladesh','afganisthan','bhutan','nepal','india','pakisthan','sri lanka'];
# country = input('Enter a country name: ')
# if country in saarc:
#     print(country, ' is a member of saarc');

# print('program termiateed')



# saarc = ['bangladesh','afganisthan','bhutan','nepal','india','pakisthan','sri lanka'];
# country = input('Enter a country name: ')
# if country in saarc:
#     print(country, ' is a member of saarc');
# else:
#     print(country, ' is not a memebr of saarc')

# print('program termiateed')



#  checking grade 

# marks = input('Enter a mark here:');
# marks = int(marks)

# if marks >= 80:
#     print('A+')
# elif marks >= 70:
#     print('A');
# elif marks >= 60:
#     print('A-')
# elif marks >= 50:
#     print('B')
# else:
#     print('F')



# marks = input('Enter a mark here');
# marks = int(marks)

# if marks >= 80:
#     grade = 'A+'
# elif marks >= 70:
#     grade = 'A'
# elif marks >= 80:
#     grade = 'A-'
# elif marks >= 70:
#     grade = 'A'
# elif marks >= 60:
#     grade = 'A-'
# elif marks >= 40:
#     grade = 'F'
# print('your grade is ', grade)



# task - 1

# num = input('Enter a number to check negative or positive: ')
# num = int(num)
# if num >= 0:
#     print(num,' is positive number')
# elif num <= 0:
#     print(num, ' is negative number')
# else:
#     print('not a number')




# task - 2

# num = input('Enter a number')
# num = int(num)
# if (num % 2) == 0:
#     print('even number')
# else: 
#     print('Odd number')




# =========== leap year ===========


# year = input('year : ')
# year = int(year)

# if year % 4 != 0:
#     print('not a leap year')
# else:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('yes')
#         else :
#             print('no')
#     else:
#         print('Yes')





# year = input('year : ')
# year = int(year)

# if year % 400 == 0:
#     print('yes')
# elif year % 100 == 0:
#     print('no')
# elif year % 4 == 0:
#     print('yes')
# else:
#     print('no')




# year = input('year : ')
# year = int(year)

# if year % 100 != 0 and year % 4 == 0:
#     print('Yes')
# elif year % 100 == 0 and year % 400 == 0:
#     print('Yes')
# else:
#     print('no')



# ================= task - 3 ==================


# year = input('year : ')
# year = int(year)

# if year % 100 != 0 and year % 4 == 0:
#     print(year, ' is a leap year')
# elif year % 100 == 0 and year % 400 == 0:
#     print(year, ' is a leap year')
# else:
#     print(year, ' is not a leap year')





# ------------------- Loop ------------------


# for i in range(10):
#     print('I want to be a great programmer')



# import turtle

# turtle.shape("turtle")
# turtle.speed(1)

# for i in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# turtle.exitonclick()




# import turtle
# turtle.shape('turtle')
# turtle.speed(1)

# for i in range(3):
#     turtle.forward(100)
#     turtle.left(120)

# turtle.exitonclick()




# count = 0
# for i in range (50):
#     count += 1
# print(count)



# count = 0
# num = 1
# for i in range(50):
#     count += num
#     num = num + 1
# print(count)


# count = 0
# for num in range(51):
#     count = count + num
# print(count)

# count = 0
# for num in range(1, 51):
#     count += num
# print(count)



# for i in range(1, 11):
#     print(i)


# for i in range(1, 20, 5):
#     print(i)


# count = 0
# for num in range(1, 101):
#     if num % 5 == 0:
#         print(num)
#         count += num
# print('sum is : ', count)



# count = 0
# for num in range(5, 101, 5):
#     print(num)
#     count += num
# print(count)



# .: turtle example:.  


# import turtle

# turtle.shape('turtle')
# turtle.speed(1)

# for i in range(20):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

# turtle.exitonclick()



# import turtle

# turtle.shape('turtle')
# turtle.speed(2)

# for side_length in range(50, 100, 10):
#     for i in range(6):
#         turtle.forward(side_length)
#         turtle.left(90)

# turtle.exitonclick()




# names = ['shakil','babu','fahim','morshed','torikus','sadik']
# for friends in names:
#     print(friends)



# li = list(range(11))
# print(li)



# even = list(range(2, 21, 2))
# print(even)



# odd = list(range(1, 20, 2))
# print(odd)



# -------> namata <---------


# num = input('Enter a number:')
# num = int(num)

# m = 1
# while m <= 10:
#     print(num, 'x', m, '=', num * m)
#     m += 1




# import turtle

# turtle.color('red')
# turtle.speed(5)

# counter = 0
# while counter < 36:
#     for i in range(4):
#         turtle.forward(100)
#         turtle.right(90)
#     turtle.right(10)
#     counter += 1

# turtle.exitonclick()





# import turtle

# height = 7
# width = 7

# turtle.speed(2)

# turtle.penup()

# for y in range(height):
#     for x in range(width):
#         turtle.dot()
#         turtle.forward(20)
#     turtle.backward(20 * width)
#     turtle.right(90)
#     turtle.forward(20)
#     turtle.left(90)

# turtle.exitonclick()




# while True:
#     n = input('please enter a number(0 to exit): ')
#     n = int(n)
#     if n == 0:
#         break
#     print('Square of ', n , 'is', n * n)



# while True:
#     n = input('Enter a number (0 to exit) : ')
#     n = int(n)
#     if n < 0:
#         print('We only allow positive number here try again')
#         continue
#     if n == 0:
#         break
#     print('Square of ', n , 'is', n * n )



# terminate_program  = False
# while not terminate_program:
#     num1 = input('please enter a number: ')
#     num1 = int(num1)
#     num2 = input('please enter another number: ')
#     num2 = int(num2)

#     while True:
#         operation = input('please enter add / sub or quit to exit: ')
        
#         if operation == 'quit':
#             terminate_program = True
#             break
#         if operation not in ['add','sub']:
#             print('unknown opeartion')
#             continue
#         if operation == 'add':
#             print('Result is ', num1 + num2)
#             break
#         if operation == 'sub':
#             print('Result is ', num1 - num2)
#             break



"""
    => again basics <= 
"""


# a, b, c = 'torikus','sadik','raihan'
# print(a)
# print(b)
# print(c)



# one value to multiple variables 

# x = y = z  = 'tomato'
# print(x)
# print(y)
# print(z)



# unpack a collection 


# fruits = ['apple','banana','cherry']
# a, b, c = fruits

# print(a)
# print(b)
# print(c)



# --< Gobal variable 

# a = 'awesome '
# def myfunc():
#     print('python is ' + a)

# myfunc()


# --< local and global (both)



# x = 'awesome'

# def myfunc():
#     x = 'fantastic'
#     print('python is ' + x)

# myfunc()
# print('python is ' + x)


# --> global (keyword)

# x = 'awesome'
# def myfunc():
#     global x
#     x = 'fantastic'

# myfunc()
# print('python is ' + x)



"""
    ==? Data types ?==

"""

# -> complex

# x = 1j 
# print(x)
# print(type(x))


# x = 1001j
# print(x)



# import random 

# print(random.randint(1, 3))


# --> Type casting 

# a = int(1)
# b = int(1.29)
# c = int('3090')

# print(a, b, c)



# a = 'hello, world'
# print(a[1])
# # output???



# -> loop through a string 

# a  = 'torikus sadik'
# for indexes in a:
#     print(indexes)



