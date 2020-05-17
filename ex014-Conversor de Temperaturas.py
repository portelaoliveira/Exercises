'''
EXERCÍCIO 014: Conversor de Temperaturas

Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.
'''
def menu_inicial():
    print('-'*82)
    print(' '*5,'Programa para Conversão de Temperaturas: Celsius, Kelvin e Fahrenheit.')
    print('-'*82,'\n')
    print('='*35,'By Portela','='*35,'\n')
    print('-'*82)
    print(' '*5,'1. Converter de graus Celsius (°C) para graus Fahrenheit (°F): ')
    print('-'*82)
    print(' '*5,'2. Converter de graus Fahrenheit (°F) para graus Celsius (°C): ')
    print('-'*82)
    print(' '*5,'3. Converter de Kelvin (K) para graus Celsius (°C): ')
    print('-'*82)
    print(' '*5,'4. Converter de graus Celsius (°C) para Kelvin (K): ')
    print('-'*82)
    print(' '*5,'5. Converter de graus Fahrenheit (°F) para Kelvin(K): ')
    print('-'*82)
    print(' '*5,'6. Converter de Kelvin (K) para graus Fahrenheit (°F): ')
    print('-'*82)

def cel_fahr():
    print('-'*82)
    C = float(input('Entre com a temperatura em graus Celsius: '))
    print('-'*82)
    F = C * (9 / 5) + 32
    print('-'*82)
    print(f'Valor da temperatura em graus Fahrenheit: {F:.2f}°F')
    print('-'*82)

def fahr_cel():
    print('-'*82)
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    print('-'*82)
    C = (F - 32) * (5 / 9)
    print('-'*82)
    print(f'Valor da temperatura em graus Celsius: {C:.2f}°C')
    print('-'*82)
        
def kelv_cel():
    print('-'*82)
    K = float(input('Entre com a temperatura em Kelvin: '))
    print('-'*82)
    C = K - 273.15
    print('-'*82)
    print(f'Valor da temperatura em graus Celsius: {C:.2f}°C')
    print('-'*82)
        
def cel_kelv():
    print('-'*82)
    C = float(input('Entre com a temperatura em graus Celsius: '))
    print('-'*82)
    K = C + 273.15
    print('-'*82)
    print(f'Valor da temperatura em Kelvin: {K:.2f}K')
    print('-'*82)
        
def fahr_kelv():
    print('-'*82)
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    print('-'*82)
    K = (F - 32)/1.8 + 273.15
    print('-'*82)
    print(f'Valor da temperatura em Kelvin: {K:.2f}K')
    print('-'*82)
        
def kelv_fahr():
    print('-'*82)
    K = float(input('Entre com a temperatura em Kelvin: '))
    print('-'*82)
    F = (K - 273.15)*1.8 + 32
    print('-'*82)
    print(f'Valor da temperatura em graus Fahrenheit: {F:.2f}°F')
    print('-'*82)
        
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
        
        print('-'*82)
        escolha = input('Escolha por favor o tipo de conversão que deseja realizar: ')
        print('-'*82)
    
        if escolha == '1':
            cel_fahr()
            n = str(input('Deseja sair do programa: [S/N]')).upper()
                
        if escolha == '2':
            fahr_cel()
            n = str(input('Deseja sair do programa: [S/N]')).upper()
                       
        if escolha == '3':
            kelv_cel()
            n = str(input('Deseja sair do programa: [S/N]')).upper()
                   
        if escolha == '4':
            cel_kelv()
            n = str(input('Deseja sair do programa: [S/N]')).upper()
        
        if escolha == '5':    
            fahr_kelv()
            n = str(input('Deseja sair do programa: [S/N]')).upper()
                
        if escolha == '6': 
            kelv_fahr()
            n = str(input('Deseja sair do programa: [S/N]')).upper()
            
    sair_programa()
