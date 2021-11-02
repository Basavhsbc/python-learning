# To define class in python
class Employee:
    def __init__(self, name: str, salary: float, experience=0):
        assert salary >=0, f" salary value is {salary} and should be equal to zero or greater than zero and it cant be negative"
        assert experience >=0, f"experience value is {experience} and should be equal to zero or greater than zero and it cant be negative"
        self.name=name
        self.salary=salary
        self.experience=experience
    def employe_package(self):
        return self.salary * self.experience

# Create first object from class Employee
employee1=Employee("Devops Consultant", 100, 7)

employee2=Employee("Cloud Devops Consultant", 30000, 10)

print(employee1.employe_package())

print(employee2.employe_package())