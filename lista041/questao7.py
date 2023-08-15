'''
7) Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo.
'''

num = int(input("Insira um número inteiro, por favor:"))
if (num >= 0):
    print(f"O módulo do número {num} é igual a {num}.")
else:
    print(f"O módulo do número {num} será equivalente a {num * -1}.")