'''
4) Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”.
'''

num = int(input("Insira um número inteiro:"))

if (num % 5 ==0 and num % 4 ==0):
    print(f"O número {num} é divisível por 4 e 5.")
else:
    print(f" O valor {num} não é divisível por 4 e 5.")