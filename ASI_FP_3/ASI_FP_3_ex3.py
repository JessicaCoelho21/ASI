#Semana 3, exercício 2

#Ler ficheiro e carregar todas as pessoas do sexo feminino numa hashtable:
fp = open('alunos.txt', 'r')
alunos = {}

for conteudo in fp:
    conteudo = conteudo.strip().split(';')
    #O dicionário alunos vai passar a ter como keys os números dos alunos e como valores uma lista de dados
    alunos[conteudo[0]] = conteudo[1:5]

print(alunos)

for i in alunos:
    if(alunos[i][2] == 'F'):
        print(alunos.__getitem__(i))

#Pesquisas na hashtable por número
numero = input("Introduza o número do aluno: ")
print("Número do aluno: ", numero, "--> %s" % (", ".join(alunos[numero])))

#Calcular a média de idades a partir da hashtable
media = 0
contador = 0
soma = 0

for i in alunos:
    soma = soma + int(alunos[i][1])
    contador += 1

media = soma / contador
print("Média das idades: ", media, " anos")

fp.close()