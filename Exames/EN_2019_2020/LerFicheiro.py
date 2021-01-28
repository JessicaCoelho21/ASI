def ler():
    despesas = {}
    nome_despesa = {}
    val_data = {}
    valores = {}
    
    with open("despesas2019.csv") as fp:
        for linhas in fp:
            linhas = linhas.strip().split(";")
            
            if linhas[1] in val_data.keys():
                valores["valores", "dataPagamento"] = float(linhas[2]), linhas[3]
                val_data[linhas[1]].update(valores)
            else:
                val_data[linhas[1]] = {"valores": float(linhas[2]), "dataPagamento": linhas[3]}

            if linhas[0] in despesas.keys():
                nome_despesa={linhas[1]:{"valores": float(linhas[2]), "dataPagamento": linhas[3]}}
                despesas[linhas[0]].update(nome_despesa)
            else:
                despesas[linhas[0]] = {linhas[1]: {"valores":float(linhas[2]), "dataPagamento": linhas[3]}}

    #print(val_data.items())
    #print(despesas.items())

    return despesas
