'''
EXERCÍCIO 027: Primeiro e Último Nome de uma Pessoa

Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro = Ana
Último = Souza
'''
continuar = True
while continuar:
    n = str(input('Digite seu nome completo: ')).split()
    print(f'Muito prazer em te conhecer.')
    print(f'Seu primeiro nome é {n[0].title().strip()}.')
    print(f'Seu último nome é {n[-1].title().strip()}.')
    n = str(input('Deseja continuar: [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False

