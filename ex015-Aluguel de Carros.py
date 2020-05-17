'''
EXERCÍCIO 015: Aluguel de Carros

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
'''
def menu_inicial():
    print('='*15,'By Portela','='*15,'\n')
    print('-'*15,'Aluguel de carros','-'*15)
    
def valor_pago():
    t = (d * 60) + (r * 0.15)
    print(f'Total a pagar é de R${t:.2f}.')
        
def lin():
    print('-'*29)
    
from time import sleep
def fim():
    for contagem in range(0,1):
        print('Saindo...')
        sleep(6)
        print('Muito obrigado, volte sempre.')

if __name__=='__main__':
    menu_inicial()
    n = 'N'
    while n == 'N':
        lin()
        d = float(input('Quantos dias alugados? '))
        lin()
        lin()
        r = float(input('Quantos Km rodados? '))
        lin()
        valor_pago()
        lin()
        n = str(input('Deseja sair do programa? ')).upper()
        lin()
    fim()
