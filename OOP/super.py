

# super() -> Function used to give access to the methods of a parent class
#            Returns a temporary object of a parent class when used 


# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

    

# class Square(Rectangle):

#     def __init__(self, length, width):
#         super().__init__(length, width)

    
#     def area(self):
#         return self.length * self.width

    
# class Cube(Rectangle):

#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height 

#     def volume(self):
#         return self.length * self.width * self.height

# square = Square(3, 3)
# cube = Cube(3, 3, 3)

# print(square.area())
# print(cube.volume())



# --------------------------------------------------------------------------------


# --> w3 example 

# class Parent:

#     def __init__(self, txt):
#         self.message = txt 
    
#     def printmessage(self):
#         print(self.message)


# class Child(Parent):
    
#     def __init__(self, txt):
#         super().__init__(txt)


# x = Child('hello, and welcome here! ')
# x.printmessage()




# another example from 'programiz'


# in python super() has two major use cases:
#   - Allows us to avoid using the base class name explicity
#   - Working with multiple inheritance 




# class Mammal(object):
#     def __init__(self, mamalName):
#         print(mamalName, ' is a warm-blooded animal')


# class Dog(Mammal):
#     def __init__(self):
#         print('Dog has four legs')
#         super().__init__('Dog')


# d1 = Dog()


# another example with multiple inheritance 


# class Animal:
#     def __init__(self, Animal):
#         print(f'{Animal} is an animal')
    

# class Mammal(Animal):
#     def __init__(self, mamalName):
#         print(f'{mamalName} is a warm-blooded animal.')
#         super().__init__(mamalName)

# class NonWingedMammal(Mammal):
#     def __init__(self, NonWingedMammal):
#         print(f'{NonWingedMammal} can\'t fly')
#         super().__init__(NonWingedMammal)


# class NonMarineMammal(Mammal):
#     def __init__(self, NonMarineMammal):
#         print(f'{NonMarineMammal} can\'t swim')
#         super().__init__(NonMarineMammal)

    
# class Dog(NonMarineMammal, NonWingedMammal):
#     def __init__(self):
#         print('Dog has 4 legs')
#         super().__init__('Dog')


# d = Dog()
# print('')
# bat = NonMarineMammal('Bat')






