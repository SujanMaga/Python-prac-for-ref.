class Employee:
    company = "Sony"
    salary = 900
    salaryBounus = 200
    # totalSalary = 1000
    @property
    def totalSalary(self):
        return self.salary + self.salaryBounus

    @totalSalary.setter
    def totalSalary(self,val):
        self.salaryBounus = val - self.salary



e = Employee()
print(e.totalSalary)
e.totalSalary = 1200
print(e.salaryBounus)