"""
EXERCÍCIO 077: Contando Vogais em Tupla
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras: # Analisar cada elemento da tupla de 'aprender' até 'futuro'.
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # Analisar cada letra da plavra, ex: 'aprender'.
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            