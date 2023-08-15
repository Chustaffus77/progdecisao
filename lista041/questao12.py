'''
12) Desenvolver um programa que pergunte 5 números inteiros e identifique o maior número e o menor número.
'''

n1 = int(input("Insira o 1º número:"))
n2 = int(input("Insira o 2º número:"))
n3 = int(input("Insira o 3º número:"))
n4 = int(input("Insira o 4º número:"))
n5 = int(input("Insira o 5º número:"))

maior = n1

if (maior < n2):
     maior = n2

if (maior < n3):
     maior = n3

if (maior < n4):
     maior = n4

if (maior < n5):
     maior = n5

menor = n1

if (menor > n2):
        menor = n2

if (menor > n3):
        maior = n3

if (menor > n4):
        menor = n4

if (menor > n5):
        menor = n5



print(f"O maior número dessa lista é {maior}, já o menor equivale a {menor}.")