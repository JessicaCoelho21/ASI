def ler():
    despesas = {}
    val_data = {}
    valores = {}

    with open("despesas2019.csv") as fp:
        for linhas in fp:
            linhas = linhas.strip().split(";")

            # se o nome da despesa já existir na hashtable val_data
            if linhas[1] in val_data.keys():
                # atribuir o valor e a data à hashtable valores
                # linhas[2] -> Valor a pagar em €
                valores["valores", "dataPagamento"] = float(linhas[2]), linhas[3]
                # atualiza a hashtable com os valores da hashtable valores
                val_data[linhas[1]].update(valores)
            else:
                # senão, preenche diretamente o valor e a data
                val_data[linhas[1]] = {"valores": float(linhas[2]), "dataPagamento": linhas[3]}

            # se o mês já existir na hashtable despesas
            if linhas[0] in despesas.keys():
                # atribui o nome da despesa e uma hashtable com os valores e a data à hashtable nome_despesa
                nome_despesa = {linhas[1]: {"valores": float(linhas[2]), "dataPagamento": linhas[3]}}
                # atualiza a hashtable despesas com os valores da hashtable nome_despesa
                despesas[linhas[0]].update(nome_despesa)
            else:
                #senão, preenche diretamente o valor e a data
                despesas[linhas[0]] = {linhas[1]: {"valores": float(linhas[2]), "dataPagamento": linhas[3]}}

    # print(val_data.items())
    # print(despesas.items())

    return despesas