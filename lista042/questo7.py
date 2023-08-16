'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.
'''

n1 = float(input("Digite um número, por obséquio:"))
n2 = float(input("Agora insira mais um:"))

if (n1 > n2):
    print(f"O número {n1} é maior, e o {n2} é o menor.")
else:
    if(n1 == n2):
        print("Ambos os números são iguais.")
    else:
        print(f"O número {n2} é maior, e o {n1} é o menor.")