'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

un = input("Insira um Estado Brasileiro:")

if(un == "RJ"):
    print("Esse estado está inserido na Região Sudeste, é o Rio de Janeiro.")
else:
    if (un == "SP"):
        print("Esse Estado está dentro da região Sudeste, é São Paulo.")
    else:
        if (un == "MG"):
            print("Esse Estado está dentro da região Sudeste, representa Minas Gerais.")
        else:
            if (un == "ES"):
                print("Esse Estado está dentro da região Sudeste, Saudosa terra de Espírito Santo!")
            else:
                print("Esse estado não está dentro da região Sudeste.")

