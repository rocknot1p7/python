l=eval(input())
result=[[0,0,0],[0,0,0]]
for i in range(len(l)):
    for j in range(len(l[0])):
        result[j][i]=l[i][j]
for r in result:
    print(r)
