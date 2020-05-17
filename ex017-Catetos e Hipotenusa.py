'''
EXERCÍCIO 017: Catetos e Hipotenusa

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''
def lin():
    print(' '*5,'-'*100)

def lin1():
    print('-'*110)
    
def menu_inicial():
    print('='*50,'By Portela','='*50,'\n')
    print(''*1,'-'*37,'Analisando um triângulo retângulo','-'*37,'\n')
    lin()
    print(' '*7,'1. Entar com o valor do cateto oposto e cateto adjacente e obter o valor da hipotenusa.')
    lin()
    print(' '*7,'2. Entrar com o valor da hipotenusa e o cateto oposto e obter o valor do cateto adjacente.')
    lin()
    print(' '*7,'3. Entrar com o valor da hipotenusa e o cateto adjacente e obter o valor do cateto oposto.')
    lin()
    print(' '*7,'4. Entra com o valor do ângulo em graus e a hipotenusa e obter o valor do cateto oposto.')
    lin()
    print(' '*7,'5. Entra com o valor do ângulo em graus e a hipotenusa e obter o valor do cateto adjacente.')
    lin()
    print(' '*7,'6. Entrar com o valor do ângulo em graus e o cateto oposto e obter o valor da hipotenusa.')
    lin()
    print(' '*7,'7. Entrar com o valor do ângulo em graus e o cateto adjacente e obter o valor da hipotenusa.')
    lin()
    print(' '*7,'8. Entrar com o valor do cateto oposto e a hipotenusa e obter o valor do ângulo em graus.')
    lin()
    print(' '*7,'9. Entrar com o valor do cateto adjacente e a hipotenusa e obter o valor do ângulo em graus.')
    lin()
    print(' '*7,'10. Entrar com o valor do cateto oposto e a cateto adjacente e obter o valor do ângulo em graus.')
    lin()
    
import math    

def co_ca():
    lin1()
    co = float(input('Comprimento do cateto oposto: '))
    lin1()
    ca = float(input('Comprimento do cateto adjacente: '))
    lin1()
    hi = math.sqrt(co**2 + ca**2)
    lin1()
    print(f'O valor da hipotenusa é {hi:.2f}.')
    lin1()

def hi_co():
    lin1()
    hi = float(input('Comprimento da hipotenusa: '))
    lin1()
    co = float(input('Comprimento do cateto oposto: '))
    lin1()
    ca = math.sqrt(hi**2 + co**2)
    lin1()
    print(f'O valor do cateto adjacente é {ca:.2f}.')
    lin1()
    
def hi_ca():
    lin1()
    hi = float(input('Comprimento da hipotenusa: '))
    lin1()
    ca = float(input('Comprimento do cateto adjacente: '))
    lin1()
    co = math.sqrt(hi**2 + ca**2)
    lin1()
    print(f'O valor do cateto oposto é {co:.2f}.')
    lin1()
    
def a_hi():
    lin1()
    a = float(input('Ângulo em graus: '))
    lin1()
    hi = float(input('Comprimento da hipotenusa: '))
    lin()
    co = math.sin(math.radians(a))*hi
    lin1()
    print(f'O valor do cateto oposto é {co:.2f}.')
    lin1()
    
def an_hi():
    lin1()
    a = float(input('Ângulo em graus: '))
    lin1()
    hi = float(input('Comprimento da hipotenusa: '))
    lin1()
    ca = math.cos(math.radians(a))*hi
    lin1()
    print(f'O valor do cateto adjacente é {ca:.2f}.')
    lin()

def a_co():
    lin1()
    a = float(input('Ângulo em graus: '))
    lin1()
    co = float(input('Comprimento do cateto oposto: '))
    lin1()
    hi = co/math.sin(math.radians(a))
    lin1()
    print(f'O valor da hipotenusa é {hi:.2f}.')
    lin1()
    
def a_ca():
    lin1()
    a = float(input('Ângulo em graus: '))
    lin1()
    ca = float(input('Comprimento do cateto adjacente: '))
    lin1()
    hi = ca/math.cos(math.radians(a))
    lin1()
    print(f'O valor da hipotenusa é {hi:.2f}.')
    lin1()
    
def co_hi():
    lin1()
    co = float(input('Comprimento do cateto oposto: '))
    lin1()
    hi = float(input('Comprimento da hipotenusa: '))
    lin1()
    a = math.asin(co/hi)*180/3.1415926
    lin1()
    print(f'O valor do ângulo é {a:.2f}.')
    lin1()
    
def ca_hi():
    lin1()
    ca = float(input('Comprimento do cateto adjacente: '))
    lin1()
    hi = float(input('Comprimento da hipotenusa: '))
    lin1()
    a = math.acos(ca/hi)*180/3.1415926
    lin1()
    print(f'O valor do ângulo é {a:.2f}.')
    lin1()
    
def ca_co():
    lin1()
    co = float(input('Comprimento do cateto oposto: '))
    lin1()
    ca = float(input('Comprimento do cateto adjacente: '))
    lin1()
    a = math.atan(co/ca)*180/3.1415926
    lin1()
    print(f'O valor do ângulo é {a:.2f}.')
    lin1()

from  time import sleep
def sair_programa():
    for contagem in range(0,1):  
        print('saindo...')
        sleep(6)  
        print('Obrigado, volte sempre.')

if __name__=='__main__':
    menu_inicial()
    
    n = 'N'
    while n == 'N':
        
        lin1()
        escolha = str(input('Informe sua opção para realizar a operação: '))
        lin1()
        
        if escolha == '1':
            co_ca()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()
            lin1()
        if escolha == '2':
            hi_co()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()
            lin1()
        if escolha == '3':
            hi_ca()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()
            lin1()
        if escolha == '4':
            a_hi()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()
            lin1()
        if escolha == '5':
            an_hi()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()
            lin1()
        if escolha == '6':
            a_co()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()
            lin1()
        if escolha == '7':
            a_ca()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()
            lin1()
        if escolha == '8':
            co_hi()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()
            lin1()
        if escolha == '9':
            ca_hi()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()
            lin1()
        if escolha == '10':
            ca_co()
            lin1()
            n = str(input('Deseja sair do programa: ')).upper()  
            lin1()

    sair_programa()
