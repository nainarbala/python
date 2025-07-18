class Employee:
    def greet(self):
        print("Greet Employeee")

class Person:
    def greet(self):
        print("Greet Person")

class Manager(Employee, Person):
    pass

emp = Employee()
print(emp.greet())