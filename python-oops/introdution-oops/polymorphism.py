class Parrot:
    def fly(self):
        print("Parrot can fly")
    def swim(self):
        print("Parrot cant swim")

class Penguin:
    def fly(self):
        print("Pengiun cant fly")
    def swim(self):
        print("Pengiun can swim")
# common interface
def flying_test(bird):
    bird.fly()

# instantiate objects
blu=Parrot()
peggy=Penguin()
# Passing objects
flying_test(blu)
flying_test(peggy)


