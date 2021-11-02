# Different data type in python, how data type works in python
# In build Data type are actually instance of class
# employee="Software Engineer"
# employee_salary=50000
# employee_role="Devops Consultant"
# employee_experience=10.9
# print(type(employee))
# print(type(employee_salary))
# print(type(employee_role))
# print(type(employee_experience))
# To define your own data type, use class 
# To define class in python
class Employee:
    def __init__(self):
        print("I am created")
    def employe_package(self,x,y):
        return x*y

# Create first object from class Employee
employee1=Employee()
employee1.salary=5000
employee1.experience=11.00
employee1.role="Devops Consultant"
# print(type(employee))
# print(type(employee.salary))
# print(type(employee.experience))
# print(type(employee.role))
# Understanding how default data type works and it access class from string class
#  
# random_string="basav"
# print(random_string.upper())
#print(type(random_string))
# Create second object from class Employee
employee2=Employee()
employee2.salary=30000
employee2.experience=11.00
employee2.role="Cloud Devops Consultant"
# To call methods from class using object reference
print(employee1.employe_package(employee1.salary,employee1.experience))
print(employee2.employe_package(employee2.salary,employee2.experience))