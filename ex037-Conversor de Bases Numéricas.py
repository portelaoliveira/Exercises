'''
EXERCÍCIO 037: Conversor de Bases Numéricas

Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
a base de conversão:
- 1 para Binário
- 2 para Octal
- 3 para Hexadecimal
'''
def lin():
    print('-'*76)

def inicio():
    print('-='*16,'BY PORTELA','-='*16,'\n')
    print(' '*19,'-'*6,'Conversor de Bases Numéricas','-'*6)
    lin()
    print('Escolha uma das bases para conversão:\n')
    lin()
    print('[ 1 ] Converter para BINÁRIO.')
    lin()
    print('[ 2 ] Converter para OCTAL.')
    lin()
    print('[ 3 ] Converter para HEXADECIMAL.')
    lin()

def bi():
    lin()
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n).strip('0b')))
    lin()
    
def oc():
    lin()
    print('{} convertido para OCTAL é igula a {}.'.format(n, oct(n).strip('0o').upper()))
    lin()
    
def he():
    lin()
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n).strip('0x').upper()))
    lin()

def erro():
    lin()
    print('Você digitou uma opção inválida, tente novamente.')
    lin()
        
if __name__=='__main__':
    
    inicio()
    continuar = True
    while continuar:
        lin()
        n = int(input('Digite um número inteiro: '))
        lin()
        lin()
        escolha = str(input('Sua opção: '))
        lin()
        
        if escolha == '1':
            bi()
        elif escolha == '2':
            oc()
        elif escolha == '3':
            he()
        else:
            erro()
        lin()
        n1 = str(input('Deseja continuar? [S/N]')).upper()
        lin()
        if n1 == 'N':
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
