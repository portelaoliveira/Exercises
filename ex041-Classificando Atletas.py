"""
EXERCÍCIO 041: Classificando Atletas

A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date

continuar = True
while continuar:
    
    an = int(input('Ano de nascimento: '))
    ano = date.today().year
    ano1 = ano - an

    if ano1 <= 9:
        print(f'O atleta tem {ano1} anos.')
        print('Classificação: MIRIM')

    elif ano1 > 9 and ano1 <= 14:
        print(f'O atleta tem {ano1} anos.')
        print('Classificação: INFANTIL')
    
    elif ano1 > 14  and ano1 <= 19:
        print(f'O atleta tem {ano1} anos.')
        print('Classificação: JÚNIOR')
    
    elif ano1 > 19 and ano1 <= 25:
        print(f'O atleta tem {ano1} anos.')
        print('Classificação: SÊNIOR')

    else:   
        print(f'O atleta tem {ano1} anos.')
        print('Classificação: MASTER')
    
    n = str(input('Deseja continuar? [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
