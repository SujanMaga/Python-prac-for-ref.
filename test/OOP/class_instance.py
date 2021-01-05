class Employee:
    company = "Google"
    salary = 100

sujan = Employee()
anuska = Employee()
sujan.salary = 300
anuska.salary = 400


print(sujan.salary)
print(anuska.salary)
# print(ansuka.age)
# above line throws error as age is not present in instance or class

# 1st pritority is isntance attributes then only class attributes
