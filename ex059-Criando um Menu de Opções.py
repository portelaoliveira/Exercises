"""
EXERCÍCIO 059: Criando um Menu de Opções

Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Números
[ 5 ] Sair do Programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep

def inicio():
    print('{:=^30}'.format('PROGRAM BY PORTELA'))
    sleep(2)
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))

    return a, b

def menu_opção():
    print('''
        [ 1 ] Somar.
        [ 2 ] Multiplicar.
        [ 3 ] Obter o maior número.
        [ 4 ] Digitar novos números.
        [ 5 ] Sair do programa.
    ''')

    return int((input('>>>> Qual é sua opção? ')))

def soma(x, y):
    return (x + y)

def multiplicar(x, y):
    return (x * y)

def maior_menor(x, y):
    if x > y:
        return x

    else:
        return y

def sair_programa():
    print('FINALIZANDO...')
    sleep(2)
    print('Fim do programa! Volte sempre!')

def menssage(opção, a, b):
    if opção == 1:
            print('A soma entre {} e {} é {}. '.format(a, b, soma(a, b)))

    elif opção == 2:
        print('A multiplicação entre {} e {} é {}. '.format(a, b, multiplicar(a, b)))
    
    elif opção == 3:
        print('Entre {} e {} o maior valor é {}. '.format(a, b, maior_menor(a, b)))

    elif opção == 4:
        print('Informe os números novamente: ')
        a = int(input('Primeiro valor: '))
        b = int(input('Segundo valor: '))
        
    elif opção == 5:
        sair_programa()    

    else:
        print('Opção inválida. Tente novamente.')

    sleep(3)

    return a, b

def main():

    a, b = inicio()
    opção = 0 
    while opção != 5:
        opção = menu_opção()
        a, b = menssage(opção, a, b)
    
if __name__ == "__main__":
    main()
