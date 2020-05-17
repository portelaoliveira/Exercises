"""
EXERCÍCIO 072: Número por Extenso

Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

continuar = True
while continuar:

    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente. ', end='')

    print(f'Você digitou o número {cont[n]}. ')

    resp = str(input('Deseja continuar? [S/N] ')).upper()
    if resp == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
        