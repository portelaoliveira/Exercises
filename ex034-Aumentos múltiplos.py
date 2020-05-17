'''
EXERCÍCIO 034: Aumentos Múltiplos

Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais, o aumento é de 15%.
'''
continuar = True
while continuar:
    s = float(input('Qual é o salário do funcionário? R$'))
    if s <= 1250:
        a = 1.15*s
        print(f'Quem ganhava R${s:.2f} passa a ganhar R${a:.2f} agora.')
    else:
        b = 1.10*s
        print(f'Quem ganhava R${s:.2f} passa a ganhar R${b:.2f} agora.')
        
    n = str(input('Deseja continuar? [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
