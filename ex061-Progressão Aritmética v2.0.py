"""
EXERCÍCIO 061: Progressão Aritmética v2.0

Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""

def inicio():
    print('{:=^100}'.format('Progressão Aritmética'))
    
inicio()

continuar = True
while continuar:

    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razão da PA: '))
    n = int(input('Qual termo deseja obter? '))

    termo = primeiro
    c = 1
    while c <= n:
        print("{} ".format(termo), end="-> ")
        termo += razao
        c += 1
    print('FIM')
    n1 = str(input('Digitar novamente novos valores? [S/N] ')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False 
