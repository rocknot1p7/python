# Object
# The entity having state and behavior is called object
# Everything in python is an object
# class dont have it's own memory whenever we declare an object,
# the memory is allocated to the class
class car:
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
# Method : The function associated with an object is termed as method
# below is the display method 
    def display(self):
        print(self.modelname,self.year)
c1=car("Toyota",2016)
c1.display()
