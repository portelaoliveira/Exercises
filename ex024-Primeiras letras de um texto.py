'''
EXERCÍCIO 024: Verificando as Primeiras Letras de um Texto

Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''
continuar = True
while continuar:
    cid = str(input('Em qual cidade você nasceu? ')).strip()
    print(cid[:5].upper() == 'SANTO')
    n = str(input('Deseja continuar: [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte semore.')
        continuar = False

