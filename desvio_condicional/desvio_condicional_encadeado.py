'''
Crie um programa que pergunte um número ao usuário.
Em seguida o programa deve informar se o número inserido está abaixo de 100 e 200 ou acima de 200.
'''

num = int(input("Informe um número:"))

if ( num < 100):
    print(f"{num} está abaixo de 100.")

else:
    if (num <= 200):
        print(f"{num} está entre 100 em 200.")

    else:
        print(f"{num} é maior que 200, parabéns!")




print("FIM DO PROGRAMA")