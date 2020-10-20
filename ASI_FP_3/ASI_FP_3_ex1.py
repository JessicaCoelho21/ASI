#Semana 3, exercício 1

#Carregar conteúdo do ficheiro numa hashtable
fp = open('input.txt')
#dicionário
alunos = {}

for conteudo in fp:
    conteudo = conteudo.strip().split(';')
    alunos[conteudo[0]] = conteudo[1]

print(alunos)

#Ler o número de aluno a partir do teclado e fazer as pesquisas na hashtable pelo número lido
numero = input("Que número de aluno deseja procurar?: ")
print("Número do aluno: ", numero, ", Nome do aluno: ", alunos[numero])

fp.close()