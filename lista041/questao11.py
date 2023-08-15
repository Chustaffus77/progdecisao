'''
Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''
print("A seguir, insira um número de 3 algarismos!")
n1 = int(input("Coloque um número:"))

if (n1 < 100):
    print("Esse número não corresponde ao formato exigido.")

else:
  print(f" O algarismo que simboliza as centenas é equivalente a {n1//100}.")
