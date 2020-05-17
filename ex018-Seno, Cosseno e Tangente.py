'''
EXERCÍCIO 018: Seno, Cosseno e Tangente

Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
n = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print(f'O ângulo digitado foi {n}°, logo SIN({n})={s:.2f}.')
print(f'O ângulo digitado foi {n}°, logo COS({n})={c:.2f}.')
print(f'O ângulo digitado foi {n}°, logo TAN({n})={t:.2f}.')
