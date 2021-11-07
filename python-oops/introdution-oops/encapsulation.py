# Encapsulation concept in python is about restricting access to attributes and methods from class
## To restrict access to attributes and methods using single or double underscore
class Computer:
    # To initialise object with attributes while creating object itself.
    def __init__(self,price):
        self.__price=price

    def shell_price(self):
        print(f"Selling price of computer is {self.__price}")
        return self.__price
    def setPrice(self,price):
        self.__price=price

# To create object from class "Computer"
computer=Computer(35000)
# To change selling price and it will not allow to change value of the attributes..
computer.__price=40000
print(f"price of computer for shell before change is {computer.shell_price()}")
# To change value of class or object attribute, use setter method
computer.setPrice(40000)
print(f"price of computer for shell after change is {computer.shell_price()}")