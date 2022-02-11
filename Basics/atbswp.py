

# -> print()
# 
# print('Assalamu alaikum')  




# -> input()

# name = input('Enter your name here: ')
# print('your name is: ', name)



# -> len()

# name = 'torikus sadik'
# count = len(name)
# print(count)


# -> str()

# number = 2022
# number_to_string = str(number)
# print(number_to_string)



# -> int()

# snum = '2022'
# sToNum = int(snum)
# print(sToNum)
# print(sToNum + 2)

# --- float to integer 

# fl = 12.22
# integer = int(fl)
# print(integer)




# -> float()

# int to float 

# real = 10
# floating = float(real)
# print(floating)







"""

    =====================================
    ============ Flow control ===========
    ===================================== 

"""


# pass check 

# name = input('please enter your name: ')
# password = input('Please enter your password here:')

# if name == 'Shakil' or name == 'shakil':
#     print('hello, ', name)
# if password == 'shakkhi':
#     print('welcome to your world!', name)
# else:
#     print('Correct your password dude!')



# elif 

# name = input('name: ')
# age = int(input('age: '))

# if name == 'shakil':
#     print('hey,', name)
# elif age < 12:
#     print('You are not shakil, kiddo')
# elif age > 2000:
#     print('you are alien')
# elif age > 100:
#     print('hi dado you are not shakil')






# --> while loop :

# spam = 0
# while spam < 5:
#     print('aaaaaa a a a aa ')
#     spam += 1


# name = ''
# while name != 'torikus':
#     print('Please type your name:')
#     name = input()
# print('thank you')




# while True:
#     print('please type your name: ')
#     name = input()
#     if name == 'torikus':
#         break
# print('Thank you!')




# while True:
#     print('Who are you')
#     name = input()
#     if name != 'torikus':
#         continue
#     print('hello, torikus. what is the password dude?')
#     password = input('Enter your pass: ')
#     if password == 'sandgrid':
#         break

# print('-------< Access granded! >-------- ')





"""
            ======= Functions =======
"""



# def hello():
#     print('howdy!')
#     print('Howdy!!!')
#     print('Hello there')

# hello()
# hello()
# hello()


# def satement with parameters:

# def hello(name):
#     print('hello', name)

# hello('shakil babu')
# hello('fahim morshed')




# random numbers 


# import random

# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'yeah'
#     elif answerNumber == 4:
#         return 'Reply hazy try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'very doubtful'

# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)





# local and global scope 



# def spam():
#     eggs = 12 # local variable 
# spam()
# print(eggs)



def spam():
    eggs = 90
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0
    print(ham)

spam()




















