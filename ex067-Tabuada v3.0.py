"""
EXERCÍCIO 067: Tabuada v3.0

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
"""

while True:

    print('-'*45)
    n = int(input('Digite um número para ver a sua tabuada: '))
    if n < 0:
        break
    x = 0
    for c in range (0, 10):
        x += 1
        print(f'{n} x {x} = {n*x}')
    print('-'*45)

print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')
