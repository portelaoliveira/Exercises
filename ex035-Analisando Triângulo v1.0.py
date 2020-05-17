'''
EXERCÍCIO 035: Analisando Triângulo v1.0

Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''
continuar = True
while continuar:
    a = float(input('Primeiro segmento: '))
    b = float(input('Segundo segmento: '))
    c = float(input('Terceiro segmento: '))

    if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
        print('Os segmentos acima PODEM FORMAR um triângulo.')
    else:
        print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')

    n = str(input('Deseja continuar? [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
