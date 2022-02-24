
# -> class
# -> Instantiate
# -> Method 
# -> Dote Ecpression

# class IceCream:
#     def eat(self):
#         print('yum!')
    
# cream = IceCream()
# cream.eat()


# -> Constructor

# class IceCream:
#     def __init__(self):
#         self.scoops = 3


#     def eat(self):
#         print('yum!')
    
# cream = IceCream()
# print(cream.scoops)



# -> Attribute


# class IceCream:
#     def __init__(self):
#         self.scoops = 3


#     def eat(self, scoops):
#         self.scoops -= scoops

# cream = IceCream()
# print(cream.scoops)
# cream.eat(2)
# print(cream.scoops)



# -> practice 



# class IceCream:
#     def __init__(self):
#         self.scoops = 3

#     def eat(self, scoops):
#         if self.scoops < scoops:
#             print('Not enough bits left!')
#         else:
#             self.scoops -= scoops
    
#     def add(self, scoops):
#         self.scoops += scoops 
    
# cream = IceCream()
# cream.eat(5)



# -> Creating lights 


# -> class 
# -> Method 
# -> Dot Expression
# -> constructor 
# -> Attribute 
# -> Practice 


# class Light:
#     def __init__(self):
#         self.on = False
    
#     def toggle(self):
#         self.on = not self.on

# light = Light()
# light.toggle()
# print(light.on)



# => 

# class Light:
#     def __init__(self):
#         self.on = False
    
#     def is_on(self):
#         return self.on
    
#     def toggle(self):
#         self.on = not self.on
    
# light = Light()
# print(light.is_on())
# light.toggle()
# print(light.is_on())





# class Light:
#     on = False

# a = Light()
# b = Light()

# Light.on = True 
# print(Light.on)
# a.on = True
# print(a.on)
# print(b.on)










