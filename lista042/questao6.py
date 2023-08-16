'''
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
'''

nas = int(input("Em que ano você nasceu?"))
atu = int(input("Qual é o ano atual?"))

if(atu>nas):
    print(f"Você tem {atu-nas} anos? Ou vai fazer? Estou correto?")
else:
    print("Os dados inseridos estão incorretos.")