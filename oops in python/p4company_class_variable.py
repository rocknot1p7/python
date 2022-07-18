class MyCompany:
    #Class Variable
    growth = 0.1
            
    def __init__(self, compname, revenue, employeesize):
        #Instance Variables
        self.name = compname
        self.revenue = revenue
        self.no_of_employees = employeesize

MyCompany.growth
