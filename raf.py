

# --> dictionary 

# student = {'name': 'shakil babu','age': 21, 'courses': ['python3','javascript']}
# print(student['name'])


# student = {'name' : 'shakil babu','name':'fahim morshed', 'name':'torikus sadik'}
# print(student)


# student = {'name':'tonmoy','age': 20}
# print(type(student))

# student ={
#     'name': 'Ali hasan',
#     'age' : 20,
#     'byear' : 2002,
#     'CGPA' : 3.60,
#     'present' : True,
#     'absent' : False,
#     'favcolors' : ['white','red','blue']
# }
# print(len(student))


# car = {
#     'name' : 'corolla',
#     'cc' : 1000,
#     'model' : 'z3'
# }
# print(car.get('cc'))

# car = {
#     'name' : 'corolla',
#     'cc' : 1000,
#     'model' : 'z3'
# }
# print(car.keys())


# car = {
#     'name' : 'corolla',
#     'cc' : 1000,
#     'model' : 'z3'
# }
# print(car.values())


# car = {
#     'name' : 'corolla',
#     'cc' : 1000,
#     'model' : 'z3'
# }
# print(car.items())



# car = {
#     'name' : 'corolla',
#     'cc' : 1000,
#     'model' : 'z3'
# }

# if 'cc' in car:
#     print("yeah, we have 'cc' in our dictionary. ")

# else:
#     print("Sorry! we don't have that key in our dictionary. ")



# car = {
#     'name' : 'corolla',
#     'cc' : 1000,
#     'model' : 'z3'
# }
# car['cc'] = 1500
# print(car)



# car = {
#     'name' : 'corolla',
#     'cc' : 1000,
#     'model' : 'z3'
# }
# car.pop('cc')
# print(car)



# car = {
#     'name' : 'corolla',
#     'cc' : 1000,
#     'model' : 'z3'
# }
# car.popitem()
# print(car)


# car = {
#     'name' : 'corolla',
#     'cc' : 1000,
#     'model' : 'z3'
# }
# del car
# print(car)




# -------------> Lamda function <------------------

# x = lambda a : a + 10
# print(x(5))


# x = lambda a, b : a * b
# print(x(5, 6))


def myfunc(n):
    return lambda a : a * n
acca = myfunc(2)
print(acca(11))


# --?
# --??






