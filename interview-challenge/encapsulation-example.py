class X:
    def __init__(self):
        # Define private variable using either single underscore or double underscore
        self.__num1 = 5
        self.num2 = 2

    def display_values(self):
        print(self.__num1, self.num2)
class Y(X):
    def __init__(self):
        super().__init__()
        self.__num1 = 1
        self.num2 = 6
obj = Y()
obj.display_values()