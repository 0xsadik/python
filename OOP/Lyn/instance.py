

# --> Instance methods and attributes 

# class Book:

#     def __init__(self, title, author, pages, price):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.price = price

#     # create instance methods 
#     def getprice(self):
#         return self.price

    

# b1 = Book('war and peace','leo Tolstoy', 1225, 39.95)
# b2 = Book('The catcher in the Rye', 'JD salinger', 234, 29.95)
# print(b1.getprice())




class Book:

    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    # create instance methods 
    def getprice(self):
        if hasattr(self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price 

    def setdiscount(self, amount):
        self._discount = amount   # ( underscore (_) used with discount cause, it will not availabe outside the function)



    

b1 = Book('war and peace','leo Tolstoy', 1225, 39.95)
b2 = Book('The catcher in the Rye', 'JD salinger', 234, 29.95)
# print(b1.getprice())

# try tetting the discount 

print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())


