# To define class with Parrot
class Parrot:
    # To define class attribute
    species="bird"
    # instance attributes
    def __init__(self,name,age):
        self.name=name
        self.age=age

# To create objects from class Parrot
blu=Parrot("blu",10)
woo=Parrot("woo",15)
# To class class attribute and method from class
print(f"Blu is {Parrot.species} and its age is {blu.age}")
print(f"woo is also {Parrot.species} and its age is {woo.age}")
