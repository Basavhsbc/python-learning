# parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class and To inherite from parent class , we have to pass Parent class name as argument to child class
class Penguin(Bird):

    def __init__(self):
        # call super() function to call __init__ method from parent class to initialize it
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
# This run child class function
peggy.whoisThis()
# This run method from parent class
peggy.swim()
# This is new function created in child class
peggy.run()