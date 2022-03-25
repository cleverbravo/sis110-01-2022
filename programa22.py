#determinar si un numero es par o impar
#input          output
#8              par
#9              impar
#15             impar
#88             par

x=int(input())
residuo=x%2
if residuo==0:
    print('par')
else:
    print('impar')