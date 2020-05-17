"""
EXERCÍCIO 045: Pedra, Papel e Tesoura

Crie um programa que faça o computador jogar Jokenpô com você.
"""
from time import sleep
from random import choice

def menu():
    print('Suas opções:')
    print('[ 1 ] PEDRA')
    print('[ 2 ] PAPEL')
    print('[ 3 ] TESOURA')
        
if __name__=='__main__':
    
    continuar = True
    while continuar:
        menu()
        lista = ['PEDRA', 'PAPEL', 'TESOURA']
        user = int(input('Qual é sua jogada? '))
        jogador = lista[user-1]
        computador = choice(lista)
        
        if jogador == lista[0] and computador == lista [1]:
            print('JO')
            sleep(2)
            print('KEN')
            sleep(2)
            print('PÔ!!!')
            sleep(1)
            print('\nJogador: {}'.format(jogador))
            print('Computador: {}'.format(computador))
            print('\n')
            print('Computador VENCEU! {} ganha de {}!'.format(lista[1], lista[0]))
        elif jogador == lista[0] and computador == lista[2]:
            print('JO')
            sleep(2)
            print('KEN')
            sleep(2)
            print('PÔ!!!')
            sleep(1)
            print('\nJogador: {}'.format(jogador))
            print('Computador: {}'.format(computador))
            print('\n')
            print('Jogador VENCEU! {} ganha de {}!'.format(lista[0], lista[2]))
        elif jogador == lista[1] and computador == lista[0]:
            print('JO')
            sleep(2)
            print('KEN')
            sleep(2)
            print('PÔ!!!')
            sleep(1)
            print('\nJogador: {}'.format(jogador))
            print('Computador: {}'.format(computador))
            print('\n')
            print('Jogador VENCEU! {} ganha de {}!'.format(lista[1], lista[0]))
        elif jogador == lista [1] and computador == lista[2]:
            print('JO')
            sleep(2)
            print('KEN')
            sleep(2)
            print('PÔ!!!')
            sleep(1)
            print('\nJogador: {}'.format(jogador))
            print('Computador: {}'.format(computador))
            print('\n')
            print('Computador VENCEU! {} ganha de {}!'.format(lista[2], lista[1]))
        elif jogador == lista[2] and computador == lista[0]:
            print('JO')
            sleep(2)
            print('KEN')
            sleep(2)
            print('PÔ!!!')
            sleep(1)
            print('\nJogador: {}'.format(jogador))
            print('Computador: {}'.format(computador))
            print('\n')
            print('Computador VENCEU! {} ganha de {}!'.format(lista[0], lista[2]))
        elif jogador == lista [2] and computador == lista[1]:
            print('JO')
            sleep(2)
            print('KEN')
            sleep(2)
            print('PÔ!!!')
            sleep(1)
            print('\nJogador: {}'.format(jogador))
            print('Computador: {}'.format(computador))
            print('\n')
            print('Jogador VENCEU!{} ganha de {}!'.format(lista[2], lista[1]))
        else:
            print('JO')
            sleep(2)
            print('KEN')
            sleep(2)
            print('PÔ!!!')
            sleep(1)
            print('\nJogador: {}'.format(jogador))
            print('Computador: {}'.format(computador))
            print('\n')
            print('EMPATE!')
                
        n1 = str(input('Deseja continuar? [S/N]')).upper()
        if n1 == 'N':
            print('MUito obrigado, volte sempre.')
            continuar = False
