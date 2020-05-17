'''
EXERCÍCIO 023: Separando Dígitos de um Número

Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Exemplo;
Dezena: 3
Centena: 8
Milhar: 1
'''
def lin():
    print('-'*35)
    
continuar = True
while continuar:
    lin()
    num = int(input('Informe um número: '))
    lin()
    nstr = str(num)
    qtnum = len(nstr)
    lin()
    print(f'Analisando o número {num}, temos: \n')
    lin()
    if qtnum == 4:
        unidade = nstr[3:4]
        dezena = nstr[2:3]
        centena = nstr[1:2]
        milhar = nstr[0:1]
        lin()
        print(f'Unidade: {unidade}')
        lin()
        lin()
        print(f'Dezena: {dezena}')
        lin()
        lin()
        print(f'Centena: {centena}')
        lin()
        lin()
        print(f'Milhar: {milhar}')
        lin()
        lin()
        resposta = str(input('Deseja continuar? [S/N]')).upper()
        lin()
        if resposta == 'N':
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
    if qtnum == 3:
        unidade = nstr[2:3]
        dezena = nstr[1:2]
        centena = nstr[0:1] 
        lin()
        print(f'Unidade: {unidade}')
        lin()
        lin()
        print(f'Dezena: {dezena}')
        lin()
        lin()
        print(f'Centena: {centena}')
        lin()
        lin()
        resposta = str(input('Deseja continuar? [S/N]')).upper()
        lin()
        if resposta == 'N':
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
    if qtnum == 2:
        unidade = nstr[1:2]
        dezena = nstr[0:1]
        lin()
        print(f'Unidade: {unidade}')
        lin()
        lin()
        print(f'Dezena: {dezena}')
        lin()
        lin()
        resposta = str(input('Deseja continuar? [S/N]')).upper()
        lin()
        if resposta == 'N':
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
    if qtnum == 1:
        unidade = nstr[0:1]
        lin()
        print(f'Unidade: {unidade}')
        lin()
        lin()
        resposta = str(input('Deseja continuar? [S/N]')).upper()
        lin()
        if resposta == 'N':
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
    if qtnum > 4:
        lin()
        print('Informe por favor um número de 0 a 1000: ')
        lin()
        lin()
        resposta = str(input('Deseja continuar? [S/N]')).upper()
        lin()
        if resposta == 'N':
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
