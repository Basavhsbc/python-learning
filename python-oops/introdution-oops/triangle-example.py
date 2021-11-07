# To understand python oops concept better
# Illustrating calculating perimeter of triangle using python oops concept.
class Triangle:
    # To initialize object with initial value
    def __init__(self,side,base,side1):
        self.side=side
        self.base=base
        self.side1=side1
    # custom method to calculate perimeter of triangle
    def calculate_perimeter(self):
        return self.side + self.base + self.side1
# To create object using triangle class
triangle=Triangle(10,15,5)
# To access method from triangle class
print(triangle.calculate_perimeter())


