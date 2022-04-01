#escribir un programa para leer la altura y la base de un rectangulo R1
#leer la altura y la base de un rectangulo R2
#mostrar por pantalla si el segundo rectangulo tiene el doble de las dimensiones del primero
#input      output
#3  4
#6  8       El segundo rectangulo es el doble del primero
#2  4
#3  5       El segundo rectangulo no es el doble del primero

b=float(input())
h=float(input())

b2=float(input())
h2=float(input())

if b2==2*b and h2==2*h:
    print('El segundo rectangulo es el doble del primero')
else:
    print('El segundo rectangulo no es el doble del primero')

