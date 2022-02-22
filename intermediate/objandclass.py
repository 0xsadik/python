# object and class 


# -> example - 0


# class Car:
#     name = 'premio'
#     color = 'white'

#     def start():
#         print('starting engine....')

# print('Name of the car is:', Car.name)
# print('Color of the car is :', Car.color)
# Car.start()




# -> example - 1

# class Car :
#     name = ''
#     color = ''
    
#     def start():
#         print('staring engine ...')
    
# Car.name = 'Axio'
# Car.color = 'Red'
# print('Name of the car is: ', Car.name)
# print('Color of the car is : ', Car.color)
# Car.start()



# -> example - 2


# class car:
#     name = ''
#     color = ''

#     def start(self):
#         print('car is satarting...')
    
# my_car = car()
# my_car.name = 'Alison'
# print(my_car.name)
# my_car.start()



# -> self a little bit 

# class check:
#     def __init__(self):
#         print('Adress of self = ', id(self))

# obj = check()
# print('Address of class object = ', id(obj))



# -< another example 

# class car():
#     # init method or constructor 
#     def __init__(self, model, color):
#         self.model = model
#         self.color = color 

#     def show(self):
#         print('Model is', self.model)
#         print('color is', self.color)

# audi = car('audi a4', 'blue')
# ferrari = car('ferrari 488', 'green')

# audi.show()
# ferrari.show()






