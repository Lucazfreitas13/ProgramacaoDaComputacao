import math
contador = 0
soma = 0
resp = 's'
while resp == 's' or resp == 'S':
    numero=float(input('Digite um número: '))
    soma=soma+numero
    contador=contador+1
    resp=input('Deseja continuar (S/N)?')
    media=soma/contador
    print('A média dos números digitados é %.2f' %media)