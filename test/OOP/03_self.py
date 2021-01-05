class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

sujan = Employee()
sujan.salary = 1000
sujan.getSalary()             # Employee.getSalary(harry)

