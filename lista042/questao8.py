'''
Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior, o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final.
'''

n1 = float(input("Digite o 1º número:"))
n2 = float(input("Digite o 2º número:"))
n3 = float(input("Digite o 3º número:"))

maior = n1

if(n1 < n2):
    maior = n2

if(n2 < n3):
        maior = n3

print(f"O valor {maior} é o maior entre os números apresentados.")