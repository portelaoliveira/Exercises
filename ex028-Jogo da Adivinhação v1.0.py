'''
EXERCÍCIO 028: Jogo da Adivinhação v1.0

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
from  time import sleep

def lin():
    print('-'*56)
    
def inicio():
    print('='*26,'GAME','='*26,'\n')
    print('-'*23,'BY PORTELA','-'*23)
    print('-*-'*19)
    print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
    print('-*-'*19)
    
def processando():
    lin()
    print('PROCESSANDO...')
    lin()
    sleep(3)
    
def sair_jogo():
    lin()
    print('SAINDO DO GAME...')
    lin()
    sleep(3)
    
inicio()
continuar = True
while continuar:
    computador = randint(0, 5)
    jogador = int(input('Em que número eu pensei? '))
    if jogador != computador:
        processando()
        lin()
        print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')
        lin()
        lin()
        n = str(input('Quer tentar novamente? [S/N]')).upper()
        lin()
        if n == 'N':
            sair_jogo()
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
    else:
        processando()
        lin()
        print(f'PARABÉN! Você conseguiu me vencer, eu pensei no número {computador} e você também!')
        lin()
        lin()
        n = str(input('Quer tentar novamente? [S/N]')).upper()
        lin()
        if n == 'N':
            sair_jogo()
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
