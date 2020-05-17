"""
EXERCÍCIO 070: Estatísticas em Produtos

Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$ 1000.
C) Qual é o nome do produto mais barato.
"""
print('-'*20)
print('CONTROLE DE COMPRAS')
print('-'*20)

cont = total = totalmil = menor = 0
nome_produto_menor = ''

while True:
    nome_produto = str(input('Nome do produto: ')).upper()
    valor = float(input('Preço: R$'))

    cont += 1
    total += valor
    if valor > 1000:
        totalmil += 1
    
    if cont == 1 or valor < menor:
        menor = valor
        nome_produto_menor = nome_produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra é de R${total:.2f}. ')
print(f'Temos {totalmil} produto(s) custando mais de R$1000.00. ')
print(f'O produto mais barato é a(o) {nome_produto_menor} que custa R${menor:.2f}. ')
