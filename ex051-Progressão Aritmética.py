"""
EXERCÍCIO 051: Progressão Aritmética

Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
def inicio():
    print('{:=^100}'.format('Progressão Aritmética'))
    
inicio()
continuar = True
while continuar:
    
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    n = int(input('Quantos elementos deseja exibir? '))

    ultimo = primeiro + (n - 1) * razao
    ultimo += 1

    for c in range (primeiro, ultimo, razao):
        print(c, end='->')
    print('FIM')
    
    n1 = str(input('Deseja continuar? [S/N]')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
