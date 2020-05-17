'''
EXERCÍCIO 019: Sorteando um Item na Lista

Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

Um professor quer sortear um dos seus quatros alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''
import random
import os
def lin():
    print('-'*51)
    
def inicio():
    print('='*19,'By Portela','='*20,'\n')
    print(' '*3,'-'*17,'Sorteio','-'*17,'\n')

def menu_inicial():
    lin()
    print('-'*14,'Istruções de comandos','-'*14)
    lin()
    lin()
    print("Quer continuar ? [S/N]: ")
    lin()
    print('S - Adicionar mais pessoas na lista do sorteio. ')
    lin()
    print('N - Realizar o sorteio. ')
    lin()

def salvar_nomes(nome_arquivo, nome):
    with open(nome_arquivo, 'a') as file:
        file.write(nome.title()+"\n")

def sortear_nome(nome_arquivo):
    nomes = []
    with open(nome_arquivo,'r') as file:
        for nome in file:
            nomes.append(nome)
    lin()
    print(f'O nome sorteado foi: {random.choice(nomes)}.')
    lin()

if __name__ == "__main__":
    
    inicio()
    continuar = True
    nome_arquivo = 'arq01.txt'
    while continuar:
        lin()
        nome = input("Insira um nome: ")
        lin()
        salvar_nomes(nome_arquivo, nome)
        menu_inicial()
        lin()
        resposta = input("Quer continuar ? [S/N]: ").upper()
        lin()
        if resposta == 'N':
            sortear_nome(nome_arquivo)
            os.remove(nome_arquivo)
            continuar = False
