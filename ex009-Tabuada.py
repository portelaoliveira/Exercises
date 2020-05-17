'''
EXERCÍCIO 009: Tabuada

Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''
def lin():
    print('-'*12)
n = int(input('Digite um número para ver a sua tabuada: '))
x = 0
lin()
while x <=10:
    print(f'{n} x {x} = {n*x}')
    x += 1
lin()
