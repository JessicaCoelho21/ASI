# Semana 3, exercício 2

# Ler o ficheiro para um dicionário, que tenha nif como chave e o valor uma hashtable cuja chave é a matrícula
# e o valor o IUC
nifs = {}
fp = open('dados.txt', 'r')

for linha in fp:
    veiculo = {}

    #remove os espaços em branco e divide por ;
    linha = linha.strip().split(';')

    #valida se o nif já existe como key na lista de nifs
    if linha[0] in nifs.keys():
        #coloca na chave existente NIF
        veiculo = nifs[linha[0]]
        #Novo carro, cria lista matrícula como chave e IUC como valor
        veiculo[linha[1]] = linha[2]
        #adiciona o veículo ao NIF existente
        nifs[linha[0]] = veiculo

    else:
        veiculo[linha[1]] = linha[2]
        nifs[linha[0]] = veiculo

fp.close()
print(nifs)

# Imprimir os dados (matrículas e IUC) associados um determinado NIF que deverá ser lido a partir do teclado
nif_pesquisa = input("Que NIF deseja procurar?: ")

if nif_pesquisa in nifs:
    print('NIF: ', nif_pesquisa, ', IUC: ', nifs[nif_pesquisa])

else:
    print("NIF não encontrado")

