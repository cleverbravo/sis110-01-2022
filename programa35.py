#leer los 3 parciales de 5 estudiantes y mostrar por pantalla el promedio de cada estudiante sin tomar en cuenta la nota menor.
#Input                          Output
#50 60 70                       1.-65
#55 65 75                       2.-70
#100 0 51                       3.-75.5
#10 0 0                         4.-5
#50 50 50                       5.-50
n=5
m=[]
for i in range(5):
    parciales=input()
    v=[int(k)for k in parciales.split(' ')]
    m.append(v)
k=1
for v in m:
    menor=min(v)
    print(f'{k}.-{(sum(x for x in v)-menor)/(len(v)-1)}')
    k+=1