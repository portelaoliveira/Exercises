"""
EXERCÍCIO 069: Análise de Dados do Grupo

Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
"""

cont = cont1 = cont2 = 0

while True:

    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)

    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        cont += 1

    if sexo == 'M':
        cont1 += 1

    if idade < 20 and sexo == 'F':
        cont2 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cont}.')
print(f'Ao todo são temos {cont1} homem(ns) cadastrado(s). ')
print(f'E temos {cont2} mulher(es) com menos de 20 anos. ')
