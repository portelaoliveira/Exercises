"""
EXERCÍCIO 049: Tabuada v2.0

Refaça o EXERCÍCIO 009, mostrando a tabuada de um número que
o usuário escolher, só que agora utilizando um laço for.
"""
continuar = True
while continuar:
    
    n = int(input('Digite um número para ver a sua tabuada: '))
    x = 0
    for c in range (0, 10):
        x += 1
        print(f'{n} x {x} = {n*x}')
    n1 = str(input('Deseja continuar? [S/N]')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
