'''
EXERCÍCIO 026: Primeira e Última Ocorrência de uma String

Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
'''
continuar = True
while continuar:
    n = str(input('Digite uma frese: ')).strip()
    print('A letra A aparece {} vezes na frase.'.format(n.upper().count('A')))
    print('A primeira letra A apareceu na posição {}.'.format(n.upper().find('A')+1))
    print('A última letra A apareceu na posição {}.'.format(n.upper().rfind('A')+1))
    n = str(input('Deseja continuar: [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte semore.')
        continuar = False
