# Semana 3, exercício 2

# Ler para hashtables o conteúdo do ficheiro. A hashtable de Veiculos deverá ter como
# chave o NIF e o valor será uma hashtable contendo a matricula como chave e o
# valorIUC como valor. A hashtable Imoveis deverá ter como chave o NIF e o valor será
# uma hashtable contendo o artigoMatricial e o valor será a taxaIMI.

veiculo = {}
imovel = {}
fp = open('dados2.txt', 'r')

for linha in fp:
    matricula = {}

    # remove os espaços em branco e divide por ;
    linha = linha.strip().split(';')

    if linha[0] in veiculo.keys():
        matricula = veiculo[linha[0]]
        matricula[linha[2]] = linha[3]
        veiculo[linha[0]] = matricula

    else:
        matricula[linha[2]] = linha[3]
        veiculo[linha[0]] = matricula

    artigo = {}

    if linha[0] in imovel.keys():
        artigo = imovel[linha[0]]
        artigo[linha[4]] = linha[6]
        imovel[linha[0]] = artigo

    else:
        artigo[linha[4]] = linha[6]
        imovel[linha[0]] = artigo

fp.close()
print(veiculo)
print(imovel)

# NIF que pagou mais taxa de IMI



# Total de impostos que cada NIF pagou