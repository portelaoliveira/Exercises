'''
EXERCÍCIO 030: Par ou Ímpar?

Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''
continuar = True
while continuar:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        print(f'O número {n} é PAR.')
        n = str(input('Quer continuar? [S/N]')).upper()
        if n == 'N':
            print('Muito obrigado, volte sempre.')
            continuar = False
    elif n % 2 != 0:
        print(f'O número {n} é ÍMPAR.')
        n = str(input('Quer continuar? [S/N]')).upper()
        if n == 'N':
            print('Muito obrigado, volte sempre.')
            continuar = False
