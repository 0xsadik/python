
# -> Basic class definition 


# class Book:
#     def __init__(self, title):
#         self.title = title
    
# b1 = Book('War and peace')
# b2 = Book('The catcher in the Rye')
# print(b1)
# print(b1.title)



# -> instance methods and attributes

# class Book:
#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price 

#     def getprice(self):
#         if hasattr(self, "_discount"):
#             return self.price - (self.price * self._discount)
#         else:
#             return self.price

#     def setdiscount(self, amount):
#         self._discount = amount


    
# b1 = Book('war and peace', 'Leo Tolstoy', 1225, 39.95)
# b2 = Book('The catcher in the Rye','JD salinger', 234, 29.95)

# print(b2.getprice())

# b2.setdiscount(0.24)
# print(b2.getprice())