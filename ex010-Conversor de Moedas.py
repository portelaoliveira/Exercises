'''
EXERCÍCIO 010: Conversor de Moedas

Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos Dólares ela pode comprar.
Considere U$ 1,00 = R$ 3,27
'''
n = float(input('Quanto dinheiro você tem na carteira? R$'))
d = n/4.24
e = n/4.67
print(f'Com R${n}, você pode comprar US${d:.2f} dolares e £{e:.2f} euros.')
