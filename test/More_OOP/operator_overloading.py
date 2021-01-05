class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __add__(self, other):
        return self.age + other.age

    def __floordiv__(self, other):
        return self.salary // other.salary

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Salary: {self.salary} "
    def __repr__(self):
        return f"Employee({self.name},{self.age},{self.salary})"


a = Employee("Sujan", 20, 30000)
b = Employee("Anuska", 19, 25000)
print(a//b)
    