"""
EXERCÍCIO 055: Maior e Menor da Sequência

Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

continuar = True
while continuar:

    lista = []
    for c in range (1, 6):
        n = float(input(f'Massa corporal da {c}ª pessoa: '))
        lista.append(n)

    print(f'A maior massa corporal digitada é {max(lista)}Kg. ')
    print(f'A menor massa corporal digitada é {min(lista)}Kg. ')
    n1 = str(input('Deseja continuar? [S/N] ')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
