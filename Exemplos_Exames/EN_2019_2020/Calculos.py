import LerFicheiro

# b) - Valor total de despesas por mês
def DespesasMes():
    despesaMes = LerFicheiro.ler()
    desp = {}

    # dp = mês
    for dp in despesaMes.keys():
        # n = nome da despesa
        for n in despesaMes[dp].keys():
            # t = valor a pagar (valores)
            for t in despesaMes[dp][n].keys():
                # se existir "valores" na hashtable
                if t.__contains__("valores"):
                    # se o mês existir na hashtable desp
                    if dp in desp.keys():
                        preco = desp[dp]
                        preco = preco + despesaMes[dp][n][t]
                        desp[dp] = preco
                    else:
                        preco = despesaMes[dp][n][t]
                        desp[dp] = preco

    print(desp.items())


# c) - Total de despesas por nome da despesa
def DespesasTipo():
    tipos = LerFicheiro.ler()
    despTipo = {}

    for mes in tipos.keys():
        for tp in tipos[mes].keys():
            for t in tipos[mes][tp].keys():
                if t.__contains__("valores"):
                    if tp in despTipo.keys():
                        preco = despTipo[tp]
                        preco = preco + tipos[mes][tp][t]
                        despTipo[tp] = preco
                    else:
                        preco = tipos[mes][tp][t]
                        despTipo[tp] = preco

    print(despTipo.items())


# d) - Lista de despesa sem data de pagamento
def DespesasPagar():
    tipos = LerFicheiro.ler()

    # linhas = mês
    for linhas in tipos.keys():
        # dp = tipo de despesa
        for dp in tipos[linhas].keys():
            # t = valores das chaves de dp
            for t in tipos[linhas][dp].keys():
                if t.__contains__('dataPagamento'):
                    if tipos[linhas][dp][t].__len__() == 0:
                        print(linhas + " " + dp + " = ", tipos[linhas][dp]["valores"])
