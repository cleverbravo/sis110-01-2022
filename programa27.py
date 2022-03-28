#dado n escribir un programa para calcular la cantidad total de puntos de acuerdo a la siguiente distribucion:
# .   ..   ...   .   ..   ...   .   ..   ...    etc
#n=1  n=2  n=3   n=4 n=5  n=6 ..........................

n=int(input())
gruposDeSeis=int(n/3)
residuo=n%3
total=6*gruposDeSeis
if residuo==1:
    total=total+1
if residuo==2:
    total=total+3
print(f'puntos={total}')
