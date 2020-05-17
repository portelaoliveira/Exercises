'''
EXERCÍCIO 013: Reajuste Salarial

EXERCÍCIO Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
def lin():
    print('-'*(82))
def lin1():
    print('-'*(55))
def lin2():
    print('-'*(29))
    
n = 'S'
while n == 'S':
    
    lin()
    s = float(input('Qual é o salário do funcionário? R$'))
    lin()
    lin()
    a = float(input('Qual foi o reajuste salarial em % ? '))
    lin()
    
    vca = (1+(a/100))*s
    
    lin()
    print(f'Um funcionário que ganhava R${s}, com {a}% de aumento, passa a receber R${vca:.2f}.')
    lin()
    
    lin1()
    n = str(input('Deseja repetir o procedimento com novos valores? [S/N]')).upper()
    lin1()
    
lin2()
print('Muito obrigado, volte sempre.')
lin2()
