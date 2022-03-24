#escribir un programa para leer los lados de un triangulo rectangulo (base y altura) y mostrar 
# por pantalla la hipotenusa
#input              output
#3 4                5
#7 5                8.602
#0 0                0
base=float(input())
altura=float(input())
hipotenusa=(base**2+altura**2)**.5
print(f'{hipotenusa}')

#-inf,...,-3,-2,-1,0,1,2,3,...,+inf #int
#-inf,...,-3,-2.9999999,...,-2.99999998,...,-2.999999997,-2,-1,0,1,2,3,...,+inf #float