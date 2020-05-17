'''
EXERCÍCIO 031: Custo da Viagem

Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
'''
continuar = True
while continuar:
    d = float(input('Qual é a distância da sua viagem em Km? '))
    if d <= 200:
        print(f'Você está prestes a começar uma viagem de {d}Km.')
        print(f'O preço da sua passagem será de R${d*0.5:.2f}.')
        n = str(input('Desejacontinuar? [S/N]')).upper()
        if n == 'N':
            print('Muito obrigado, volte sempre.')
            continuar = False
    else:
        print(f'Você está prestes a começar uma viagem de {d}Km.')
        print(f'O preço da sua passagem será de R${d*0.45:.2f}.')
        n = str(input('Desejacontinuar? [S/N]')).upper()
        if n == 'N':
            print('Muito obrigado, volte sempre.')
            continuar = False
