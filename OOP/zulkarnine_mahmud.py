
# All here 




# person  example 


# class Person:
#     def __init__(self, person_name):
#         self.name = person_name

#     def get_name(self):
#         return self.name

# a_person = Person('Troikus sadik')
# b_person = Person('Robot')

# print(a_person.get_name())
# print(b_person.get_name())






class Person:
    def __init__ (self, person_name, date_of_birth, ht):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.height = ht

    def get_name(self):
        return self.name 
    
    def get_summary(self):
        return f"name: {self.name}, DOB: {self.date_of_birth} and height: {self.ht}"

a_person = Person('torikus sadik','1999', '5.4 feet')
print(a_person.get_summary())