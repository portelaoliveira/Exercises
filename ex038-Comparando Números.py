'''
EXERCÍCIO 038: Comparando Números

Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
'''
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

maior = n1
if n2 > maior:
    maior = n2
    print('O SEGUNDO número é maior.')
menor = n1
if n2 < menor:
    menor = n2
    print('O PRIMEIRO número é maior.')
igual = n1
if n2 == igual:
    igual = n2
    print('Os dois números são IGUAIS.')
