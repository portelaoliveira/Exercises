"""
EXERCÍCIO 065: Maior e Menor Valores

Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre
todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores.
"""

lista = []

while True:
    n = float(input('Digite um número: '))
    lista.append(n)
    n1 = str(input('Quer continuar? [S/N] ')).upper()
    m = sum(lista)/len(lista)
    if n1 == 'N':
        break

print(f'Você digitou {len(lista)} números e a média é {m:.2f}. ')
print(f'O maior valor digitado é {max(lista)} e o menor é {min(lista)}. ')
