'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

n1 = int(input("Insira o 1º número:"))
n2 = int(input("Insira o 2º número:"))
n3 = int(input("Insira o 3º número:"))

if (n1 < n2 and n3):
    menor = n1

if (n2 < n1 and n3):
    menor = n2

if (n3 < n2 and n1):
    menor = n3



if (n1 > n2 and n3):
        maior = n1

if (n2 > n1 and n3):
        maior = n2

if (n3 > n2 and n1):
        maior = n3




if (n1 == maior and n2 ==menor):
    inter = n3

if (n1 == maior and n3 == menor):
        inter = n2

if (n3 == maior and n2 ==menor):
    inter = n1

if (n1 == menor and n2 == maior):
        inter = n3

if (n1 == menor and n3 == maior):
        inter = n2

if (n3 == menor and n2 == maior):
        inter = n1





print(f"A ordem crescente desses números é igual a {menor},{inter} e {maior}, respectivamente.")


