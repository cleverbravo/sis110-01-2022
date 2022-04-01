#dados m(filas) y n(columnas) (las dimensiones de una matriz) calcular la cantidad total de puntos de acuerdo
#a la siguiente distribucion
#.      ..      ...       ..      .       ..        ...     ..
#.      ..      ...       ..      .       ..        ...     ..
#.      ..      ...       ..      .       ..        ...     ..

n=int(input())
m=int(input())
if n%4==1 or n%4==2:
    total=(2*n-1)*m
else:
    total=(2*n)*m
print(f'{total}')