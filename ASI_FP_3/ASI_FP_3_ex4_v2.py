# Semana 3, exercício 2

# Ler para hashtables o conteúdo do ficheiro. A hashtable de Veiculos deverá ter como
# chave o NIF e o valor será uma hashtable contendo a matricula como chave e o
# valorIUC como valor. A hashtable Imoveis deverá ter como chave o NIF e o valor será
# uma hashtable contendo o artigoMatricial e o valor será a taxaIMI.
import json

veiculos = {}
imoveis = {}

with open("dados2.txt") as fp:
    for linha in fp:
        linha = linha.strip().split(";")

        if linha[0] in veiculos.keys():
            # O valor associado a veículos[linha[0]] contem uma hashtable
            # Queremos colocar mais 1 chave (matrícula) e um valor (IUC)
            veiculos[linha[0]][linha[2]] = float(linha[3])

        else:
            dados_veiculos = {}
            dados_veiculos[linha[2]] = float(linha[3])
            veiculos[linha[0]] = dados_veiculos

        if linha[4]:
            if linha[0] in imoveis.keys():
                imoveis[linha[0]][linha[4]] = float(float(linha[5]) * float(linha[6]) / 100)

            else:
                dados_imoveis = {}
                dados_imoveis[linha[4]] = float(float(linha[5]) * float(linha[6]) / 100)
                imoveis[linha[0]] = dados_imoveis

fp.close()

print(json.dumps(veiculos, ensure_ascii = False))
print("#" * 68)
print(json.dumps(imoveis, ensure_ascii = False))

# NIF que pagou mais taxa de IMI
n = ""
max = 0

for key, value in imoveis.items():
    total_imi = sum(imoveis[key].values())

    if total_imi > max:
        max = total_imi
        n = key

print(max, ", ", n)

# Total de impostos que cada NIF pagou
res = {}

for key, value in imoveis.items():
    total_imi = sum(imoveis[key].values())
    res[key] = total_imi

for key, value in veiculos.items():
    total_iuc = sum(veiculos[key].values())
    res[key] += total_iuc

print(json.dumps(res, ensure_ascii = False))
