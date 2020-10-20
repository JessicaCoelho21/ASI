#Semana 3, exercício 2

#Ler o ficheiro para um dicionário, que tenha nif como chave e o valor uma hashtable cuja chave é a matrícula
#e o valor o IUC
fp = open('dados.txt')

nif = {}
chaves = {'NIF', 'matricula', 'iuc'}

#Resolver: fazer com que apareçam todos os nif's
for conteudo in fp:
    conteudo = conteudo.strip().split(';')
    nif[conteudo[0]] = conteudo[2]

print(nif)

#Imprimir os dados (matrículas e IUC) associados um determinado NIF que deverá ser lido a partir do teclado
numero= input("Que NIF deseja procurar?: ")
print('NIF: ', numero, ', IUC: ', nif[numero])

fp.close()