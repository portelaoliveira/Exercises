'''
EXERCÍCIO 032: Ano Bissexto

Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
from datetime import date

continuar = True
while continuar:
    print('Caso você queira analisar o ano atual, coloque 0: ')
    ano = int(input('Que ano quer analisar? '))
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'O ano {ano} é BISSEXTO.')
        n = str(input('Deseja continuar? [S/N]')).upper()
        if n == 'N':
            print('Muito obrigado, volte sempre.')
            continuar = False
    else:
        print(f'O ano {ano} NÃO é BISSEXTO.')
        n = str(input('Deseja continuar? [S/N]')).upper()
        if n == 'N':
            print('Muito obrigado, volte sempre.')
            continuar = False
