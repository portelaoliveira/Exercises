"""
EXERCÍCIO 053: Detector de Palíndromo

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
"""

continuar = True
while continuar:
    
    n = str(input('Digite uma frase: ')).strip().upper() # Eliminando os espços antes e depois e deixando tudo  em maíscula
    palavras = n.split() # Gerando uma lista
    junto = ''.join(palavras) # juntando tudo em uma única string sem espaços internos
    inverso = ''

    for letra in range (len(junto) - 1, -1, -1):
        inverso += junto[letra]                     # Fazendo o invérso da frase

    print(f'O inverso de {n} é {inverso}.')
    if inverso == junto:
        print(f'Logo a frase {n} é um palíndromo.')
    else:
        print(f'Logoa a frase {n} não é um palíndromo.')
    n1 = str(input('Deseja continuar? [S/N]')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
