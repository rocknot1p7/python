class Vehicle:
    def message(self):
        print("Parent class method")

class Cab(Vehicle):
    def message(self):
        print("Child Cab class method")

class Bus(Vehicle):
    def message(self):
        print("Child Bus class method")

print("parent class method")
x = Vehicle()
x.message()

print("child class method")
y= Cab()
y.message()

print("child class method")
z = Bus()
z.message()
