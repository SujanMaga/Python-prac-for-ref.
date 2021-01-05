class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

sujanApplication = RailwayForm()
sujanApplication.name = "Sujan"
sujanApplication.train = "Janakpur Express"    
sujanApplication.printData()