'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = float(input("Insira um número que esteja entre 1 e 7:"))

if(num > 7 or num < 1):
    print("Número Inválido")

else:
    if(num == 1):
        print("Esse número equivale ao Domingo.")
    else:
        if (num == 2):
            print("Esse número equivale a Segunda-Feira.")
        else:
            if (num == 3):
                print("Esse número equivale a Terça-Feira.")
            else:
                if (num == 4):
                    print("Esse número equivale a Quarta-Feira.")
                else:
                    if (num == 5):
                        print("Esse número equivale a Quinta-Feira.")
                    else:
                        if (num == 6):
                            print("Esse número equivale a Sexta-Feira.")
                        else:
                            if (num == 7):
                                print("Esse número equivale ao Sábado.")

