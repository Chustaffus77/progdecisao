'''
6. Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

num = int(input("Insira um número inteiro:"))
num2 = int(input("Insira outro número inteiro:"))

if (num > num2 or num == num2):
    print(f"A Diferença entre o número {num} e o número {num2} é igual {num - num2}.")
else:
    print(f"A Diferença entre o número {num2} e o número {num} é igual {num2 - num}.")
