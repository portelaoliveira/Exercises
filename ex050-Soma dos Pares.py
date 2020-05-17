"""
EXERCÍCIO 050: Soma dos Pares

Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""
continuar = True
while continuar:
    
    numero = []
    par = []
    impar = []
    cont = 0
    cont1 = 0
    
    for c in range (1, 7):
        n = int(input(f'Digite o {c}ª número inteiro: '))
        numero.append(n)
        if (n % 2) == 0:
            par.append(n)
            soma = sum(par)
            cont += 1
            
        else:
            impar.append(n)
            soma1 = sum(impar)
            cont1 += 1  
            
    print(f'Os números digitados foram: {numero}.')
    print(f'A soma dos {cont} números pares {par} é {soma}.')
    print(f'A soma dos {cont1} números ímpares {impar} é {soma1}.')
    
    n1 = str(input('Deseja continuar ? [S/N]')).upper()
    if n1 == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
