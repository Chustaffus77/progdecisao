'''
2. Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, ou acima de 5000.
'''

num = float(input("Digite um número, por obséquio:"))

if (num < 1000):
    print("O número escolhido é menor ou igual a 1000.")
else:
    if (num <= 5000):
        print("O número escolhido é maior que 1000, entretanto, não é maior que 5000.")
    else:
        print("O número escolhido é maior que 1000 e 5000.")

print("FIM DO PROGRAMA")