'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

n1 = float(input("Insira o 1º número:"))
n2 = float(input("Insira o 2º número:"))
n3 = float(input("Insira o 3º número:"))

menor =  n1
if (menor < n2):
        menor = n2

if (menor < n3):
        menor = n3


maior = n1

if (maior < n2):
        maior = n2

if (maior < n3):
        maior = n3


print(f"{menor},{inter},{maior}.")






