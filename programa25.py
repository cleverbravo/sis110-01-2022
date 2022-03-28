#escribir un programa para leer un numero, luego un signo aritmetico (+,-,*,/) y finalmente otro numero
#se debe mostrar por pantalla el resultado de la operacion que se exprese.
#input              output
#3 
#+ 
#4                  7

#3 
#* 
#2                  6


a=int(input())
operacion=input()
b=int(input())

if operacion=='+':
    resultado=a+b
elif operacion=='-':
    resultado=a-b
elif operacion=='*':
    resultado=a*b
elif operacion=='/':
    resultado=a/b
else:
    print('operacion invalida')
print(resultado)