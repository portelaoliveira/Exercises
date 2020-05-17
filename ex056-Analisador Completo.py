"""
EXERCÍCIO 056: Analisador Completo

Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

continuar = True
while continuar:

    pessoas = []
    soma = 0
    cont = 0
    maior = 0

    for c in range (1,5):
        print('-'*5, f'{c}ª PESSOA', '-'*5 )
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        sexo = str(input('Sexo [M/F]: ')).upper()
        pessoas.append({ 'Nome': nome, 'Idade': idade, 'Sexo [M/F]': sexo })
        soma += idade
        média = soma/4

        if idade < 20 and sexo == 'F':
            cont += 1

        elif idade > maior and sexo == 'M':
            maior = idade
            nomeM = nome

    print(f'A média de idade do grupo é de {média:.2f} anos. ')
    print(f'O homem mais velho tem {maior} anos e se chama {nomeM}. ')
    print(f'Ao todo são(é) {cont} mulher(es) com menos de 20 anos. ')

    n = str(input('Deseja continuar? [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
