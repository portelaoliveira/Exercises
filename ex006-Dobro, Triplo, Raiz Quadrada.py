'''
EXERCÍCIO 006: Dobro, Triplo, Raiz Quadrada

Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
from math import sqrt
n = float(input('Digite um número: '))
d = n * 2
t = n * 3
r = sqrt(n)
print(f'O dobro de {n} vale {d}.')
print(f'O triplo de {n} vale {t}.')
print(f'A raiz quadrada de {n} é igual a {r:.2f}.')
