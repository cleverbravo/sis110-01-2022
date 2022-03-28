#dados m(filas) y n(columnas) (las dimensiones de una matriz) calcular la cantidad total de puntos de acuerdo
#a la siguiente distribucion
#.      ..      .       ..      .       ..
#.      ..      .       ..      .       ..
#.      ..      .       ..      .       ..
n=int(input())
m=int(input())
if n%2==0:
    cantidadDePuntosPorFila=n/2*3
else:
    cantidadDePuntosPorFila=int(n/2)*3+1
total=cantidadDePuntosPorFila*m
print(f'puntos={total}')