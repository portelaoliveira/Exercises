"""
EXERCÍCIO 054: Grupo de Maioridade

Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre
quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""


from datetime import date

continuar = True
while continuar:

    ano = date.today().year
    cont = 0
    cont1 = 0
    for c in range (1, 8):
        n = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
        a = ano - n
        if a < 21:
            cont += 1 
        
        else:
            cont1 += 1 
        
    print(f'Ao todo tivemos {cont} pessoa(s) menor(es) de idade. ')
    print(f'E também tivemos {cont1} pessoa(s) maior(es) de idade. ')
    n1 = str(input('Deseja continjuar? [S/N]')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
