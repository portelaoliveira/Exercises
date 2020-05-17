"""
EXERCÍCIO 062: Super Progressão Aritmética v3.0

Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""

from time import sleep

print('---- Super Progressão Aritimética ----')

continuar = True
while continuar:

    primeiro = int(input('Primeiro termo: '))
    razao = int (input('razão da PA: '))
    termo = primeiro 
    cont = 1
    total = 0 
    mais = 10
    while mais != 0:
            total += mais
            while cont <= total:
                    print ('{} → '.format(termo), end='')
                    termo += razao
                    cont += 1
            print('PAUSA')
            mais = int(input('Quantos termos você quer mostrar a mais?'))
            
    print('Finalizando...')
    sleep(2)
    print('==================================')
    print('Progressão finalizada com {} termos mostrado'.format(total))

    n1 = str(input('Digitar novamente novos valores? [S/N] ')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False 
