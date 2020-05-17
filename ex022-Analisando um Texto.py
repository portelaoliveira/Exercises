'''
EXERCÍCIO 022: Analisador de Textos

Crie um programa que leia o nome completo de uma pessoa e mostre:
> O nome com todas as letras maiúsculas e minúsculas.
> Quantas letras ao todo (sem considerar espaços).
> Quantas letras tem o primeiro nome.
'''
def lin():
    print('-'*80)
    
def inico():
    lin()
    nome = str(input('Digite seu nome completo: ')).strip()
    lin()
    print(f'Olá {nome.title()}.\nAnalisando seu nome temos:\n')
    lin()
    print(f'Seu nome em maiúsculas é {nome.upper()}.')
    lin()
    print(f'Seu nome em minúsculas é {nome.lower()}.')
    lin()
    print(f'Seu nome tem ao todo {len( nome.replace(" ",""))} letras.')
    lin()
    print(f'Seu primeiro nome é {nome.split()[0].title()} e ele tem {len(nome.split()[0])} letras')
    lin()
          
if __name__=="__main__":
          
    continuar = True
    while continuar:
        inico()
        lin()
        resposta = str(input('Deseja continuar? [S/N]')).upper()
        lin()
        if resposta == 'N':
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
