

# -> inheritance 


# class Vehicle :
#     """ Base class for all vehicles """

#     def __init__(self, name, manufacturer, color):
#         self.name = name
#         self.manufacturer = manufacturer
#         self.color = color 

#     def drive(self):
#         print(f'Driving {self.manufacturer} {self.name}')
    
#     def turn(self, direction):
#         print(f'Turning {self.name} to {direction}')
    
#     def brake(self):
#         print(f'{self.name} is stopping...')

# if __name__ == "__main__":
#     v1 = Vehicle('Fusion 110 Ex', 'walton','Black')
#     v2 = Vehicle('Softal Delux', 'Harley - Davidson', 'Black')
#     v3 = Vehicle('Mustang 5.0 GT  Coupe','Ford ', 'REd')

#     v1.drive()
#     v2.drive()
#     v3.drive()

#     v1.turn('left')
#     v2.turn('right')

#     v1.brake()
#     v3.brake()
#     v2.brake()





# -> inheritance anis sir

# class Phone:
#     def call(self):
#         print('you can call')
    
#     def message(self):
#         print('You can message')
    

# class Samsung:
#     def photo(self):
#         print('You can take photo')




# parent class hobe 'Shool'

class School:
    def __init__(self):
        self.name = 'Abc school'
        self.year = 1990
        self.location = 'Hatirjhil'

    def sayName(self):
        print(f'welcome to {self.name}')



class Student(School):
    def __init__(self, name, passingYear, department):
        self.name = name 
        self.passingYear = passingYear
        self.department = department

    def greeting(self):
        if self.passingYear > 2021:
            print(f'Hey {self.name}, You are currently a student!')
        elif self.passingYear > 2015:
            print(f'Hey {self.name}, You are recently graduated!')
        else:
            print(f'{self.name}, you were a student')

babu = Student('Shakil babu', 2018, 'CST')
babu.sayName()
babu.greeting()
















