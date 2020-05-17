'''
EXERCÍCIO 025: Procurando uma String Dentro de Outra

Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''
continuar = True
while continuar:
    nome = str(input('Digite seu nome completo: ')).strip()
    print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
    n = str(input('Deseja continuar: [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte semore.')
        continuar = False

