

# start from here 

# class Car:
#     name = ''
#     color = ''

#     def start():
#         print('staring the engine. . .')
    
# Car.name = 'Axio'
# Car.color = 'Black'
# print('Name of the car is: ', Car.name)
# print('Color:', Car.color)

# Car.start()




# class Car:
#     name = ''
#     color = ''

#     def start():
#         print('staring the engine')

# # creating a car obejct 
# my_car = Car()
# my_car.name = 'Allion'
# print(my_car.name)
# my_car.start()





# class Car:
#     name = ''
#     color = ''

#     def start(self):
#         print('staring the engine')

# # creating a car obejct 
# my_car = Car()
# my_car.name = 'Allion'
# print(my_car.name)
# my_car.start()


# class Car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color 

#     def start(self):
#         print("Staring ... the ... engine ...")


# my_car = Car('Corolla','White')
# print(my_car.name)
# print(my_car.color)
# my_car.start()




# class Car:
#     def __init__(self, name, color, year):
#         self.name = name
#         self.color = color 
#         self.year = year

#     def start(self):
#         print("Staring ... the ... engine ...")


# my_car = Car('Corolla','White', 2022)
# print(my_car.name)
# print(my_car.color)
# print(my_car.year)
# my_car.start()



# class Car:
#     def __init__(self, n, c):
#         self.name = n
#         self.color = c
    
#     def start(self):
#         print('Staring ... engine ...')
    
# my_car = Car('Bhugati', 'black')
# # print(my_car.name)
# print(my_car.color)



# class Car:
#     def __init__(self, n, c):
#         self.name = n
#         self.color = c
    
#     def start(self):
#         print('name:', self.name)
#         print('color:', self.color)

# my_car = Car('corolla' , 'black')
# my_car.start()



# class Car:
#     def __init__(self, n, c):
#         self.name = n
#         self.color = c
    
#     def start(self):
#         print('name:', self.name)
#         print('color:', self.color)
#         print('Staring the engine ...')

# my_car = Car('corolla' , 'black')
# Car.start(my_car)



# class Car:
#     def __init__(self, n, c):
#         self.name = n
#         self.color = c
    
#     def start(self):
#         print(f'name : {self.name}')
#         print(f'color : {self.color}')
#         print('Starting the engine ... ')

# car1 = Car('Corolla', 'white')
# car1.start()

# car2 = Car('ferarri', 'red')
# car2.start()

# car3 = Car('bhugati', 'black')
# car3.start()



# class Car:
#     def __init__(self, n, c):
#         self.name = n
#         self.color = c

#     def start(self):
#         print("Staring the enginee...")


# car = Car('Corolla','white')
# car.year = 2022

# print(car.name, car.color, car.year)



class Car:
    def __init__(self,n, m, c, y, cc):
        self.name = n
        self.manufacturer = m
        self.color = c
        self.year = y
        self.cc = cc

    def start(self):
        print(f'Car name is : {self.name}')
        print(f'Car manufacturer is : {self.manufacturer} ')
        print(f'Car color is : {self.color}')
        print(f'Year is : {self.year}')
        print(f'Car total cc is : {self.cc}')
        print('Starting the engine .. .')
    
    def brake(self):
        print('The car is braking ...')
    
    def drive(self):
        print('the car is driving now ...')
    
    def left(self):
        print('The car is turning left...')
    def right(self):
        print('The car is turning right...')

    def gear(self):
        print('The car is changing gear ')
    
car1 = Car('Corolla', 'corl', 'white','2016', '900')
car1.start()
car1.brake()
car1.drive()
car1.left()
car1.right()
car1.gear()

