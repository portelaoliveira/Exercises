"""
EXERCÍCIO 044: Gerenciador de Pagamentos

Elabore um programa que calcule o valor a ser pago de um produto,
considerando o seu preço normal, e condição de pagamento:
- À vista no dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""
def inicio():
    print('='*25, 'LOJAS PORTELA', '='*25)
    
def lin():
    print('-'*62)
    
def menu():
    lin()
    print('FORMAS DE PAGAMENTO')
    lin()
    print('[ 1 ] à vista dinheiro/cheque.')
    lin()
    print('[ 2 ] à vista cartão.')
    lin()
    print('[ 3 ] 2x  no cartão.')
    lin()
    print('[ 4 ] 3x ou mais no cartão.')
    lin()
    
if __name__=='__main__':
    
    inicio()
    continuar = True
    while continuar:
        lin()
        p = float(input('Preços das compras:'))
        lin()
        menu()
        n = int(input('Qual é sua opção? '))
        lin()
        if n == 1:
            np = (0.9) * p
            lin()
            print(f'Sua compra de R${p:.2f} vai custar R${np:.2f} no final.')
            lin()
        elif n == 2:
            np1 = (0.95) * p
            lin()
            print(f'Sua compra de R${p:.2f} vai custar R${np1:.2f} no final.')
            lin()
        elif n == 3:
            par = p/2
            lin()
            print(f'Sua compra será parcelada em 2x de R${par:.2f} SEM JUROS.')
            lin()
            lin()
            print(f'Sua compra de R${p:.2f} passará a custar R${p:.2f} no final.')
            lin()
        elif n == 4:
            lin()
            n1 = int(input('Quantas parcelas? '))
            lin()
            par1 = p/n1
            np2 = (1.2) * par1
            np3 = (1.2) * p
            lin()
            print(f'Sua compra será parcelada em {n1}x de R${np2:.2f} COM JUROS.')
            lin()
            print(f'Sua compra de R${p:.2f} passará a custar R${np3:.2f} no final.')
            lin()
        elif n > 4:
            lin()
            print('Opção inválida.')
            lin()
            
        lin()
        n2 = str(input('Deseja continuar ? [S/N]')).upper()
        lin()
        if n2 == 'N':
            lin()
            print('Muiro obrigado, volte sempre.')
            lin()
            continuar = False
