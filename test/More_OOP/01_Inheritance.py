class Employee:
    company = "Google"


    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getLanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("This is a programmer")



e = Employee()
e.showDetails()

p = Programmer()
p.getLanguage()
print(p.company)


# inherting 
# can overwrite methods and can use in inheritance