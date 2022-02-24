
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



class IceCream:
    def __init__(self):
        self.scoops = 3

    def eat(self, scoops):
        self.scoops -= scoops
    
    def add(self, scoops):
        self.scoops += scoops 
    
    



