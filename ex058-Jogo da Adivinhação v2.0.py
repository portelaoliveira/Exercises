"""
EXERCÍCIO 058: Jogo da Adivinhação v2.0

Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""

from random import randint
from time import sleep

USER_LOSE = 0
FIRST_TIME = 1
HIGHT = 2
LOW = 3
USER_WIN = 4


def lin():
    print('-'*56)


def inicio():
    print('='*26, 'GAME', '='*26, '\n')
    sleep(3)
    print('-'*23, 'BY PORTELA', '-'*23)
    sleep(3)
    print('-'*56)
    print('Sou seu computador...')
    print('-'*56)
    sleep(3)
    print('-*-'*19)
    print('Acabei de pensar em um número entre 0 e 10.')
    print('-*-'*19)
    sleep(3)
    print('-'*56)
    print('Será que você consegue adivinhar qual foi? ')
    print('-'*56)
    sleep(3)


def regras():
    print('''        ♦ Você tem 5 tentativas!
        ♦ A cada erro você perde 2 pontos.
        ♦ Se você chegar a 0 pontos você perde! \n\n''')
    sleep(5)


def processando():
    lin()
    print('PROCESSANDO...')
    lin()
    sleep(2)


def message(code, resultado_jogo):
    if code == USER_LOSE:
        lin()
        print('GAME OVER! O computador escolheu o número {}'.format(
            resultado_jogo['computador']))
        lin()
        lin()
        print('Você gastou as 5 tentativas e não ACERTOU.')
        lin()
    elif code == FIRST_TIME:
        lin()
        print('PARABÉNS!!! Você acertou de primeira.')
        lin()
    elif code == HIGHT:
        lin()
        print('ERROU... Tente um número MAIOR.')
        lin()
    elif code == LOW:
        lin()
        print('ERROU... Tente um número MENOR.')
        lin()
    else:
        lin()
        print('ACERTOU!!! Você acertou com {} tentativa(s). PARABÉNS.'.format(
            resultado_jogo['tentativas']))
        lin()
        lin()
        print('O computador escolheu o número {}.'.format(
            resultado_jogo['computador']))
        lin()
        lin()
        print('Você fez um total de {} pontos.'.format(
            resultado_jogo['pontuação']))
        lin()


def sair_jogo():
    lin()
    print('SAINDO DO GAME...')
    lin()
    sleep(2)


def jogar():
    pontuação = 10
    tentativas = 0
    jogador = ''
    acertou = False
    computador = randint(0, 10)
    
    while not acertou:

        jogador = int(input('Qual é seu palpite? '))
        tentativas += 1
        pontuação -= 2

        resultado = {
        "tentativas": tentativas,
        "computador": computador,
        "pontuação": pontuação
    }

        if jogador == computador:
            message(USER_WIN, resultado)
            acertou = True
            break

        elif tentativas == 5:
            message(USER_LOSE, resultado)
            break

        elif tentativas == 1 and jogador == computador:
            processando()
            message(FIRST_TIME, resultado)
            break

        else:
            if jogador < computador:
                processando()
                message(HIGHT, resultado)
            
            elif jogador > computador:
                processando()
                message(LOW, resultado)
            


def main():
    continuar = True
    inicio()
    regras()

    while continuar:
        jogar()
        processando()
        lin()
        n = input('Quer jogar novamente? [S/N]').upper()
        lin()
        if n == 'N':
            sair_jogo()
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False

if __name__ == "__main__":
    main()
