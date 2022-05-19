l=eval(input())
x=int(0)
y=int(99999999999)
for i in range(0,len(l),1):
    if(l[i]>x):
        x=l[i]
    if(l[i]<y):
        y=l[i]
print("Max=",x)
print("Min=",y)
