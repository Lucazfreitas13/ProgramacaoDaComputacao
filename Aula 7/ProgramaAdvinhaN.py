from random import*
num = randint(0,10)
i = 0
controle = 0

while controle == 0:
    i = i+1
    x = int(input('Digite um número entre 0 e 10: '))
    if num == x:
        print('Parabéns, você acertou em {} tentativas'.format(i))
        controle = 1
    elif num > x:
        print('O número pensado é maior')
    else:
        print('O número pensado é menor')
