"""
EXERCÍCIO 040: Aquele Clássico da Média

Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""
continuar = True
while continuar:
    
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    
    nota = (n1+n2)/2
    
    if nota > 7:
        print(f'Tirando {n1} e {n2}, a média do aluno é {nota:.1f}.')
        print('O aluno está APROVADO.')
        
    elif nota >= 5 and nota < 7:
        print(f'Tirando {n1} e {n2}, a média do aluno é {nota:.1f}.')
        print('O aluno está em RECUPERAÇÃO.')
        
    else:
        print(f'Tirando {n1} e {n2}, a média do aluno é {nota:.1f}.')
        print('O aluno está em REPROVADO.')
        
    n = str(input('Deseja continuar? [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
