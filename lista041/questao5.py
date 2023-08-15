'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno:
'''

print("Vamos tirar sua média escolar agora!")
not1 = float(input("1º nota:"))
not2 = float(input("2º nota:"))
not3 = float(input("3º nota:"))
not4 = float(input("Por fim, 4º nota:"))

media = (not1 + not2 + not3 + not4)//2

if (media >= 5):
    print("Parabéns, você está aprovado!")
else:

    print("Você infelizmente está reprovado, mas não desista!")