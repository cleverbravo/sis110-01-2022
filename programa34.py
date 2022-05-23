#leer los 3 parciales de 5 estudiantes y mostrar por pantalla el promedio de cada estudiante.
#Input                          Output
#50 60 70                       1.-60
#55 65 75                       2.-65
#100 0 51                       3.-50.333
#10 0 0                         4.-3.3333
#50 50 50                       5.-50
n=5
m=[]
for i in range(5):
    parciales=input()
    v=[int(k)for k in parciales.split(' ')]
    m.append(v)
k=1
for v in m:
    print(f'{k}.-{sum(x for x in v)/len(v)}')
    k+=1