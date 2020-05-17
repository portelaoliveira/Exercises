'''
EXERCÍCIO 039: Alistamento Militar

Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

def lin():
    print('-'*42)

def inicio():
    print('*'*16,'BY PORTELA','*'*16,'\n')
    print('-'*11,'Alistamento Militar','-'*11)
    
def mod():
    lin()
    print(f'Quem nasceu em {data} tem {a} anos em {ano}.')
    lin()
    lin()
    print(f'Você tem que se alistar IMEDIATAMENTE.')
    lin()
    
def mod1():
    f = 18 - a
    s = ano + f
    lin()
    print(f'Quem nasceu em {data} tem {a} anos em {ano}.')
    lin()
    lin()
    print(f'Ainda faltam {f} anos para o alistamento.')
    lin()
    lin()
    print(f'Seu alistamento será em {s}.')
    lin()
    
def mod2():
    fa = a - 18
    sa = ano - fa
    lin()
    print(f'Quem nasceu em {data} tem {a} anos em {ano}.')
    lin()
    lin()
    print(f'Você já deveria ter se alistado há {fa} anos.')
    lin()
    lin()
    print(f'Seu alistamento foi em {sa}.')
    lin()

if __name__=='__main__':
    
    inicio()
    continuar = True
    while continuar:
        
        lin()
        data = int(input('Ano de nascimento: '))
        lin()
        ano = date.today().year
        a = ano - data

        if a == 18:
            mod()
    
        elif a < 18:
            mod1()

        elif a > 18:
            mod2()
        
        lin()
        n = str(input('Deseja continuar: [S/N]')).upper()
        lin()
        if n == 'N':
            lin()
            print('Muito obrigado, volte sempre.')
            lin()
            continuar = False
