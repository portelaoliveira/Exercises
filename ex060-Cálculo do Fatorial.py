"""
EXERCÍCIO 060: Cálculo do Fatorial

Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""

continuar = True
while continuar:

    n = int(input('Digite um número para calcular seu Fatorial: '))
    c = n
    f = 1  
    print('Calculando {}! = '.format(n), end='')
    while c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ', end='')
        f *= c 
        c -= 1 
    print('{}'.format(f))
    n1 = str(input('Digitar outro número? [S/N]')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
        
