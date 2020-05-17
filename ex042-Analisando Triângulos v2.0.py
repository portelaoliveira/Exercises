"""
EXERCÍCIO 042: Analisando Triângulos v2.0

Refaça o EXERCÍCIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes
"""
continuar = True
while continuar:
    a = float(input('Primeiro segmento: '))
    b = float(input('Segundo segmento: '))
    c = float(input('Terceiro segmento: '))

    if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
        print('Os segmentos acima PODEM FORMAR um triângulo.')
        if a == b == c :
            print('O triângulo formado é do tipo EQUILÁTERO.')
        elif a != b != c != a:
            print('O triângulo formado é do tipo ESCALENO.')
        else:
            print('O triângulo formado é do tipo ISÓCELES.')    
    else:
        print('Os segmentos acima NÃO PODEM FORMAR um triângulo.')

    n = str(input('Deseja continuar? [S/N]')).upper()
    if n == 'N':
        print('Muito obrigado, volte sempre.')
        continuar = False
