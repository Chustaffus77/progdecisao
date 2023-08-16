'''
Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.
'''

id = int(input("Qual é a sua idade?"))
if(id < 18):
    print("Você ainda é menor de idade.")
else:
    if(id <= 65):
        print("Você já é maior de idade, mas ainda não faz parte da terceira idade.")
    else:
        print("Você já passou os 65 anos. Parabéns, que você vá ainda mais longe!")