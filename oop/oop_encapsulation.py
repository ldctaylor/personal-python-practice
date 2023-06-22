#Encapsulation is the  bundling of attributes and methods inside a single class.

#Prevents outer classes from accessing and changing attributes and methods of a class.

# Denote PRIVATE attributes with __ as prefix

class Computer:

    def __init__(self):
        self.__maxprice = 900
    
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price 

c = Computer()

c.sell()

#change the price
c.__maxprice = 1000 # <-- does not update __maxprice as is coming from outaside the class and __maxprice is private variable
c.sell() 

c.setMaxPrice(1000)
c.sell()