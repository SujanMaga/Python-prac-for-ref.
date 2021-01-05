class Employee:
    company = "Google"


    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, sir") 

    @staticmethod
    def time():
        print("The time is 9 a.m")       
sujan = Employee()
sujan.salary = 1000

sujan.greet()
sujan.time()
# Employee.greet()

# Employee.greet(sujan)
