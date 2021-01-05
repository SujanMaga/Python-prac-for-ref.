class Student():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        email = f"{fname}.{lname}@gmail.com"

    @property
    def email(self):
        if self.fname is None or self.lname is None:
            return "Email is not set, please use setter to set email"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self): 
        self.fname = None
        self.lname = None
    



    def explain(self):
        print(f"This student is {self.fname} {self.lname}")



    




a = Student("Sujan", "Magar")
b = Student("Anuska", "Gorkhali")
a.explain()

a.fname = "Ronaldo"
print(a.fname)
print(a.email)
print(a.lname)
a.email = "Lionel.messi@gmail.com"
print(a.email)
print(a.fname)
del a.email
print(a.email)