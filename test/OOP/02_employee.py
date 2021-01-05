class Employee:
    company = "Google"

sujan = Employee()
anuska = Employee()
sujan.salary = 300
anuska.salary = 400
print(sujan.company)    
print(anuska.company)    
Employee.company = "Youtube"
print(sujan.company)    
print(anuska.company)  
print(sujan.salary)
print(anuska.salary)

# class attributes
# company is directly related to class
