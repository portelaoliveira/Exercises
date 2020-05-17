'''
EXERCÍCIO 012: Calculando Descontos

Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
def lin():
    print('-'*(72))

n = 'S'
while n == 'S':
    lin()
    p = float(input('Qual é o preço do produto: R$'))
    lin()
    lin()
    d = float(input('Qual foi o desconto em %: '))
    lin()
    vcd = (1-(d/100))*p  
    lin()
    print(f'O produto que custava R${p}, na promoção de {d}% vai custar R${vcd:.2f}.')
    lin()
    lin()
    n = str(input('Deseja continuar: [S/N]')).upper()
    lin()
lin()
print('Muito obrigado, volte sempre.')
lin()
