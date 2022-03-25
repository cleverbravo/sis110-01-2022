#escribir un programa para mostrar por pantalla el primer digito de un numero
#input          output
#156            1
#4              4
#1002           1
import math

numero=int(input())
cantidadDeDigitos=int(math.log10(numero))
primerDigito=int(numero/10**cantidadDeDigitos)
print(primerDigito)