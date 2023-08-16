'''
Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, entre 5001 e 8000, ou acima de 8000.
'''

num = float(input("Mais uma vez, insira um número aqui:"))

if (num <= 1000):
    print("O número escolhido é menor ou igual a 1000.")
else:
    if (num <= 5000):
        print("O número escolhido é maior que 1000, entretanto, não é maior que 5000.")
    else:
        if (num <= 8000):
            print("O número escolhido é maior que 1000 e 5000, entretanto, não ultrapassa os 8000.")
        else:print("O número escolhido é maior que 1000,5000 e 8000.")
print("Fim do Programa")