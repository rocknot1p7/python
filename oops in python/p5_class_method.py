class Cab:
    
    #Initialise variables for first iteration
    numberofcabs  = 0
    numpassengers = 0

    def __init__(self,driver,kms,places,pay,passengers):
        self.driver = driver
        self.running = kms
        self.places = places
        self.bill = pay
        Cab.numberofcabs  =  Cab.numberofcabs + 1
        Cab.numpassengers =  Cab.numpassengers + passengers

    #Returns price of cab fare per km
    def rateperkm(self):
        return self.bill/self.running
        
    #Returns number of cabs running         
    @classmethod
    def noofcabs(cls):
        return cls.numberofcabs

    #Returns average number of passengers travelling in a cab
    @classmethod
    def avgnoofpassengers(cls):
        return int(cls.numpassengers/cls.numberofcabs)

firstcab  = Cab("Ramesh", 80, ['raigad', 'lonere'], 2200, 3)
secondcab = Cab("Suresh", 60, ['mangao', 'lonere'], 1500, 1)
thirdcab  = Cab("Raju", 20, ['mahad', 'lonere'], 680, 2)

print(firstcab.driver)
print(firstcab.rateperkm())
print(secondcab.driver)
print(secondcab.rateperkm())
print(thirdcab.driver)
print(thirdcab.rateperkm())
print("no of cabs using class method")
print(Cab.noofcabs())
print("avg no of passengers")
print(Cab.avgnoofpassengers())


