'''
EXERCÍCIO 011: Pintando Parede

Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 m².

Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2 m².
'''
l = float(input('Largura da parede em metros: '))
al = float(input('Altura da parede em metros: '))
a = l * al
r = a/2
print(f'Sua parede tem a dimensão de {l}x{al} e sua área é de {a:.3f}m².')
print(f'Para pintar essa parede, você precisará de {r:.3f}L de tinta.')
