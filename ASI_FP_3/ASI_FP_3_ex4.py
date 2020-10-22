# Semana 3, exercício 2

# Ler para hashtables o conteúdo do ficheiro. A hashtable de Veiculos deverá ter como
# chave o NIF e o valor será uma hashtable contendo a matricula como chave e o
# valorIUC como valor. A hashtable Imoveis deverá ter como chave o NIF e o valor será
# uma hashtable contendo o artigoMatricial e o valor será a taxaIMI.
fp = open('dados2.txt', 'r')

veiculos = {}
imoveis = {}
matricula = {}
artigoMatricial = {}

for conteudo in fp:
    conteudo = conteudo.strip().split(';')
    veiculos[conteudo[0]] = conteudo[2:4]
    imoveis[conteudo[0]] = conteudo[4] + ", " + conteudo[6]


print("Veículos: ", veiculos.items())
print("Imóveis: ", imoveis.items())



fp.close()
