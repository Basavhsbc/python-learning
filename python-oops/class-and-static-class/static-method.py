# To define class in python
class Employee:
    # This is class attribute
    bonus=25
    # Define empty list
    a=[]
    def __init__(self, name: str, salary: float, experience=0):
        assert salary >=0, f" salary value is {salary} and should be equal to zero or greater than zero and it cant be negative"
        assert experience >=0, f"experience value is {experience} and should be equal to zero or greater than zero and it cant be negative"
        self.name=name
        self.salary=salary
        self.experience=experience
        Employee.a.append(self)
    def employe_package(self):
        return self.salary * self.experience
    def apply_bonus(self):
        self.salary=self.salary * self.bonus
    @staticmethod
    def isinteger(num):
        if isinstance(num, float):
            return True
        elif isinstance(num, int):
            return True
        else:
            return False

# Create first object from class Employee
employee1=Employee("Devops Consultant", 100, 7)

print(Employee.isinteger(7))