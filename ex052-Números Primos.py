"""
EXERCÍCIO 052: Números Primos

Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
def inicio():
    print('{:=^60}'.format('DISCUBRA QUAL NÚMERO É PRIMO'))

inicio()
continuar = True
while continuar:
    
    cont = 0
    div = []

    n = int(input('Digite um número inteiro para saber se ele é primo ou não: '))
    print(f'O número {n} forma a seguinte sequência:')
    for c in range (1, n+1):
        if n % c == 0:
            cont += 1
            div.append(c) 
        print(c, end=' ')
    print('\n')
    print(f'Logo, o número {n} é divisível {cont} vezes. É divisível por {div}.')

    if cont == 2:
        print('E por isso ele é PRIMO.')
    else:
        print('E por isso ele NÃO É PRIMO.')
    
    n1 = str(input('Deseja continuar? [S/N]')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
