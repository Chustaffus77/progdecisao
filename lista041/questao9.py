'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = float(input("Escolha um número:"))
if (num > 0):
    print("O número escolhido está dentro do grupo dos positivos.")
else:
    if(num == 0):
        print("O número escolhido é um número nulo.")
    else:
        print("O número escolhido está dentro do grupo dos negativos.")

