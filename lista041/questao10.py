'''
10) Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado
'''

num = int(input("Insira o 1º número:"))
num2 = int(input("Insira o 2º número:"))

if (num % num2 == 0):
    print("O segundo número é um divisor do 1º número informado.")
else:
    print("O valor do 2º número não é um divisor do 1º número.")