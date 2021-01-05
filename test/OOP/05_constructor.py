class Employee:
    company = "Google"


    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
    
        print("Employee is created!")






        # special method = constructor


    def getDetail(self):
        print(f"The name of the employe is {self.name}")
        print(f"The salary of the employe is {self.salary}")
        print(f"The subunit of the employe is {self.subunit}")



    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning, sir") 

    @staticmethod
    def time():
        print("The time is 9 a.m")       


sujan = Employee("sujan",10000, "Youtube")
sujan.getDetail()