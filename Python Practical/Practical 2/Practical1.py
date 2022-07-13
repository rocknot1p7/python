# Author: Prathamesh .R Sogale
# Python Program to check if number is armstrong number
n=int(input("Enter a number to check"))
sum=int(0)
temp=int(n)
while(temp):
    sum+=int(temp%10)
    temp/=int(10)
print(sum)
if(n==sum):
    print("The given number is an armstrong number")
else:
    print("The given number is not an armstrong number")
