class Vehicle:
    def __init__(self,driver,wheels,seats):
        self.driver = driver
        self.noofwheels = wheels
        self.noofseats = seats

class Cab(Vehicle):
    pass

cab_1 = Cab('Sandy',4, 2)
print(cab_1.driver)
