'''
EXERCÍCIO 036: Aprovando Empréstimo

Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário, ou então o empréstimo será negado.
'''
continuar = True
while continuar:
    vc = float(input('Valor da casa: R$'))
    sc = float(input('Salário do comprador: R$'))
    f = float(input('Quantos anos de financiamento? '))

    m = 12*f
    p = vc/m
    s = sc*0.3

    if p <= s:
        print(f'Para pegar uma casa de R${vc:.2f} em {f} anos a prestação será de R${p:.2f}.')
        print('Empréstimo CONCEDIDO.')
    else:
        print(f'Para pegar uma casa de R${vc:.2f} em {f} anos a prestação será de R${p:.2f}.')
        print('Empréstimo NEGADO.')
        
    n = str(input('Deseja continuar? [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
