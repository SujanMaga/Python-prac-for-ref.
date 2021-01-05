class Employee:
    company = "WaiWai"
    salary = 1000
    location = "Kathmandu"
    @classmethod
    def changeSalary(cls, sal):
        cls.salary = sal

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal

e = Employee()
print(e.salary)
e.changeSalary(455)
print(Employee.salary)


# to change the class attribute

