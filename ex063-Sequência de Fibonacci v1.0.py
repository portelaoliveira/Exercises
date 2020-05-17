"""
EXERCÍCIO 063: Sequência de Fibonacci v1.0

Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma Sequência de Fibonacci.

Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)

continuar = True
while continuar:

    print('-'*30)
    n = int(input('Quantos termos você quer mostrar? '))
    print('-'*30)

    a = 0
    b = 1
    
    print('~'*100)
    print(f' {a} -> {b} ', end='-> ')

    c = 3

    while c <= n:
        d = a + b
        print(f'{d}', end='-> ')
        a = b
        b = d
        c += 1
    print('FIM')
    print('~'*100)
    n1 = str(input('Digitar outro número? [S/N] ')).upper()
    print('-'*30)
    if n1 == 'N':
        print('-'*30)
        print('Muito obrigado, volte sempre.')
        print('-'*30)
        continuar = False
