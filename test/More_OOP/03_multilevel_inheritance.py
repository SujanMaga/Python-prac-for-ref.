class Person:
    country = "Nepal"
    city = "Kathmandu"

    def takeBreath(self):
        print("I'm breathing...")

class Employee:
    company = "Honda"

    def getSalary(self):
        self.salary = salary
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I'm an Employee so I'm breathing")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print("No salary to programmer")


    def takeBreath(self):
        print("I'm an Programmer so I'm breathing")






p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
pr = Programmer()
pr.takeBreath()


# they take nearest method if it's not availabe in itself
# same with attributes
