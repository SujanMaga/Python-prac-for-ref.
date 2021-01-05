class Employee:
    company = "Visa"
    eCode = 120


class Freelancer:
    company = "Fiverr"
    level = 0


    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer(Employee, Freelancer):
    name = "Sujan"    

p = Programmer()
p.upgradeLevel()
print(p.level)

print(p.company)

# it take first property (a,b) a is taken priority


# multiple inheritance