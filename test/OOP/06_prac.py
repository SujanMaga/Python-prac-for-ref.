class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats


    def getStatus(self):
        print(f"The name of the train is: {self.name}")
        print(f"The seats availabe in the train is: {self.seats}")


    def fareInfo(self):
        print(f"The price of the ticket is {self.fare}")


    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked!! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry no seat is available.")
    
    def cancelTicket(self, seatNo):
        pass
    # maintain a list from 1 to 100 and append in the original list if cancellation




janakpur = Train("Janakpur Express: 19102", 90, 300)
janakpur.getStatus()
janakpur.bookTicket()
janakpur.getStatus()
janakpur.bookTicket()
janakpur.getStatus()

