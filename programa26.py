#leer un numero entero y mostrar por pantalla su raiz cuadrada si el primer digito es par y mayor a 3
#sino mostrar el valor elevado al cuadrado

a=input()
primerDigito=int(a[0])
x=int(a)
if primerDigito%2==0 and x>3:
    print(x**.5)
else:
    print(x**2)