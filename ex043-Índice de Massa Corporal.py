"""
EXERCÍCIO 043: Índice de Massa Corporal

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""
continuar = True
while continuar:
    
    p = float(input('Qual sua massa corporal? (Kg)'))
    a = float(input('Qual sua altura? (m)'))

    IMC = p/(a**2)

    if IMC < 18.5:
        print(f'O IMC dessa pessoa é de {IMC:.1f}.')
        print('Você está ABAIXO DO PESO normal.')
    elif 18.5 <= IMC < 25:
        print(f'O IMC dessa pessoa é de {IMC:.1f}.')
        print('PARABÉNS, Você está na faixa de PESO NORMAL.')
    elif 25 <= IMC < 30:
        print(f'O IMC dessa pessoa é de {IMC:.1f}.')
        print('Você está na faixa de SOBREPESO.')
    elif 30 <= IMC < 40:
        print(f'O IMC dessa pessoa é de {IMC:.1f}.')
        print('Você está em OBESIDADE.')
    else:
        print(f'O IMC dessa pessoa é de {IMC:.1f}.')
        print('Você está em OBESIDADE MÓRBIDA, cuidado.')
    n = str(input('Deseja continuar? [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
