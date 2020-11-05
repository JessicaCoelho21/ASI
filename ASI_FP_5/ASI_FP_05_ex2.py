# Ficha de trabalho 5, exercício 1

import re

# Separar as pessoas em dois dicionários (masculino e feminino).
# Em cada dicionário a chave é o número de telefone e o valor é o nome.

feminine = {}
masculine = {}

fp = open("dados.txt")

def people():
    for line in fp:
        line = line.strip().split(";")

        if line[2].__contains__("F"):
            feminine[line[3]] = line[0]

        elif line[2].__contains__("M"):
            masculine[line[3]] = line[0]

    print("Elementos do sexo feminino: ", feminine.items())
    print("Elementos do sexo masculino: ", masculine.items())

# Acrescentar o prefixo 00351 a todos os números de telefone
def telephone():
    for i in feminine:
        # /A --> início do input
        i = re.sub("\A", "00351", i)
        print(i)

    for j in masculine:
        # /A --> início do input
        j = re.sub("\A", "00351", j)
        print(j)
