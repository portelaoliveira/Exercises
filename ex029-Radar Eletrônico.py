'''
EXERCÍCIO 029: Radar Eletrônico

Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma
mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite.
'''
continuar = True
while continuar:
    vel = float(input('Qual é a velocidade atual do carro? '))
    mul = (vel - 80)*7
    if vel > 80:
        print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
        print(f'Você deve pagar uma multa de R${mul:.2f}.')
        print('Tenha um bom dia! Dirija com segurança!')
        n = str(input('Quer continuar? [S/N]')).upper()
        if n == 'N':
            print('Muito obrigado, volte sempre.')
            continuar = False
    else:
        print('Tenha um bom dia! Dirija com segurança!')
        n = str(input('Quer continuar? [S/N]')).upper()
        if n == 'N':
            print('Muito obrigado, volte sempre.')
            continuar = False
