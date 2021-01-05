class Programmer:
    company = 'Microsoft'
    
    def __init__(self, name, product):
        self.name = name
        self.product = product


    def getInfo(self):
        print(f"The name of {self.company} the programmer is {self.name}")    
        print(f"The product of the programmer is {self.product}")    

    
sujan = Programmer("Sujan Magar","Skype")    
anuska = Programmer("Anuska","Github")    
sujan.getInfo()
anuska.getInfo()


# class for storing info of a programmers