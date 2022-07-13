# Author: Prathamesh R. Sogale
# Python program to solve quadratic equation
import math
print("Please enter the variables for equation ax^2 +bx + c")
a=int (input("a="))
b=int (input("b="))
c=int (input("c="))
d=(b**2) - 4*a*c
r1=(-b+math.sqrt(d))/(2*a)
r2=(-b-math.sqrt(d))/(2*a)
print("root1",r1)
print("root2",r2)
