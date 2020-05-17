'''
EXERCÍCIO 008: Conversor de Medidas

Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''
n = float(input('Digite uma distância em metros: '))
print(f'{n/1000} km \n{n/100} hm \n{n/10} dam \n{n*10} dm \n{n*100} cm \n{n*1000} mm')
