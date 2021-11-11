class Human(object):
    def __init__(self, name):
        self.human_name = name

    def getHumanName(self):
        return self.human_name

    def isEmployee(self):
        return False

class IBEmployee(Human):
    def __init__(self, name, emp_id):
        super(IBEmployee, self).__init__(name)
        self.emp_id = emp_id

    def isEmployee(self):
        return True

    def get_emp_id(self):
        return self.emp_id
# Driver code
employee = IBEmployee("Mr Employee", "IB007")
print(employee.getHumanName(), employee.isEmployee(), employee.get_emp_id())