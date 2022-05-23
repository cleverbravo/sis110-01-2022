v1=[1,2]
v2=[3,4]
m=[v1,v2]
print(m)
for i in range(len(m)):
    for j in range(len(m[i])):
        m[i][j]=m[i][j]*2
print(m)