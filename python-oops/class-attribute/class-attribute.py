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

# Create first object from class Employee
employee1=Employee("Devops Consultant", 100, 7)

employee2=Employee("Cloud Devops Consultant", 300, 10)

employee3=Employee("Cloud Devops Consultant", 250, 8)

employee4=Employee("Cloud Devops Consultant", 200, 7)

# Accessing class attribute with class Employee name
# print(Employee.bonus)
# # Accessing class attribute using object
# print(employee1.bonus)
# print(employee2.bonus)
# To print class attributes and object attributes
# print(Employee.__dict__)
# # To print object attributes
# print(employee1.__dict__)
# To call apply_bonus by passing class attribute called bonus
employee1.bonus=30
employee1.apply_bonus()
print(employee1.salary)
employee2.apply_bonus()
print(employee2.salary)
# print(Employee.a)
for instance in Employee.a:
    print(instance.name)
