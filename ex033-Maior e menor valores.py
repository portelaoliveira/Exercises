'''
EXERCÍCIO 033: Maior e Menor Valores

Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
continuar = True
while continuar:
    primeiro = int(input('Primeiro valor: '))
    segundo = int(input('Segundo valor: '))
    terceiro = int(input('Terceiro valor: '))

    maior = primeiro
    if segundo > maior:
        maior = segundo
    if terceiro > maior:
        maior = terceiro
    print(f'O maior valor digitado foi {maior}.')
    
    menor = primeiro
    if segundo < menor:
        menor = segundo
    if terceiro < menor:
        menor = terceiro
    print(f'O menor valor digitado foi {menor}.')
    n = str(input('Deseja continuar? [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
