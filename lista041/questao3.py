'''
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

num = int(input("Insira um número, por obséquio:"))

if (num % 2 == 0):
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")