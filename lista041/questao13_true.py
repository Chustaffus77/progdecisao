'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Insira o 1º número:"))
b = int(input("Insira o 2º número:"))
c = int(input("Insira o 3º número:"))

if (a > b):
    aux = a

    a = b

    b = aux

#2

if (a > c):
    aux = a

    a = c

    c = aux

#garantido até aqui que a é o menor dos 3
#agora é necessário garantir que b seja menor que c

if (b > c):
    aux = b
    b = c
    c = aux

#garantido até aqui que entre b e c, o b é menor, ou seja, o c é maior de todos

print()








