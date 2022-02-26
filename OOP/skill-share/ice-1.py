
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






# from tkinter import scrolledtext


# class IceCream:

#     max_scoops = 3

#     def __init__(self):
#         self.scoops = 0

#     def eat(self, scoops):
#         if self.scoops < scoops:
#             print('Not enough bites left!')
#         else:
#             self.scoops -= scoops
        
#     def add(self, scoops):
#         self.scoops += scoops
#         if self.scoops > self.max_scoops:
#             self.scoops = 0
#             print('Too many scoops! Dropped ice cream')


# class IceCreamTruck:

#     def __init__(self):
#         self.sold = 0

#     def order(self, scoops):
#         ice_cream = IceCream()
#         self.add(ice_cream, scoops)
#         return ice_cream

#     def add(self, ice_cream, scoops):
#         ice_cream.add(scoops)
#         self.sold += scoops

# # ice_cream = IceCream()
# # ice_cream.scoops += 2
# # ice_cream.add(2)
# # ice_cream.scoops -= 3
# # ice_cream.eat(3)

# truck = IceCreamTruck()
# ice_cream1 = truck.order(3)
# ice_cream1.eat(2)
# truck.add(ice_cream1, 1)
# truck.sold

# -> practice 


# def sub(x, y):
#     return x - y

# def sub2(x, y = 0):
#     return x - y

# print(sub2(7))






class Light:

  def __init__(self, sync=None): # new - tuple
    super().__init__()
    self.on = False
    self.sync = sync

  def is_on(self):
    return self.on

  def toggle(self):
    self.on = not self.on
    if self.sync is not None:
      self.sync.toggle()

class OldLight(Light):

  def __init__(self, sync=None):
    super().__init__(sync=sync)
    self.on = False
    self.sync = sync
    self.flicker = False

  def toggle(self):
    super().toggle()
    if self.on:
      self.flicker = not self.flicker
















