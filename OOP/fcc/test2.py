


# class Item:
#     def __init__(self, name):
#         # print('I am created!')
#         # print(f'An instance created : {name}')
#         self.name = name

#     def calculate_total_price(self, x, y):
#         return x * y 

# item1 = Item("Phone")
# item1.price = 100
# item1.quantity = 5

# # print(item1.calculate_total_price(item1.price, item1.quantity))

# item2 = Item('Laptop')
# item2.price = 1000
# item2.quantity = 3
# # print(item2.calculate_total_price(item2.price, item2.quantity))


# print(item1.name)
# print(item2.name)


# class Item:
#     def __init__(self,name):
#         self.name = name 


# item1 = Item('phone')
# item2 = Item('laptop')

# print(item1.name)
# print(item2.name)



# class Person:
#     def __init__(self,name, age):
#         self.name = name 
#         self.age = age


# person1 = Person('torikus', '22')
# person2 = Person('sadik', '24')

# print(person1.name, person1.age)
# print(person2.name, person2.age)




# class Item:
#     def __init__(self,name, price, quantity):
#         self.name = name 
#         self.price = price
#         self.quantity = quantity

# item1 = Item('phone', 100, 5)
# item2 = Item('laptop', 3000, 3)

# print(item1.name)
# print(item1.price)
# print(item1.quantity)

# print(item2.name)
# print(item2.price)
# print(item2.quantity)









# class Item:
#     pay_rate = 0.5
#     def __init__(self,name: str, price: float, quantity = 0):
#         # run validations to the recieved arguments 
#         assert price >= 0 , f'Price {price} is not greater than zero!'
#         assert quantity >= 0, f'quantity {quantity} is not greater than zero! '


#         self.name = name 
#         self.price = price
#         self.quantity = quantity

#     def calculate_total_price(self):
#         return self.price * self.quantity

# item1 = Item('phone', 100, 2)
# item2 = Item('laptop', 3000, 4)




# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)



# class Item:
#     pay_rate = 0.8
#     def __init__(self,name: str, price: float, quantity = 0):
#         # run validations to the recieved arguments 
#         assert price >= 0 , f'Price {price} is not greater than zero!'
#         assert quantity >= 0, f'quantity {quantity} is not greater than zero! '


#         self.name = name 
#         self.price = price
#         self.quantity = quantity

#     def calculate_total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self):
#         return self.price * Item.pay_rate

# item1 = Item('phone', 100, 2)
# item1.apply_discount()
# print(item1.price)

























