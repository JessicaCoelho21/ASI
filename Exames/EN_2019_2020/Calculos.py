import LerFicheiro

# b)
def DespesasMes():
    despesaMes = LerFicheiro.ler()
    desp = {}
    dados = {}
    
    for dp in despesaMes.keys():
        for n in despesaMes[dp].keys():
            for t in despesaMes[dp][n].keys():
                if t.__contains__("valores"):
                    if dp in desp.keys():
                        preco = desp[dp]
                        preco = preco + despesaMes[dp][n][t]
                        desp[dp] = preco
                    else:
                        preco = despesaMes[dp][n][t]
                        desp[dp] = preco

    print(desp.items())

# c)
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

# d)
def DespesasPagar():
    tipos = LerFicheiro.ler()
    
    # linhas = mês
    for linhas in tipos.keys():
        # dp = tipo de despesa
        for dp in tipos[linhas].keys():
            # t = valores das chaves de dp
            for t in tipos[linhas][dp].keys():
                if t.__contains__('dataPagamento'):
                    if tipos[linhas][dp][t].__len__()==0:
                        print(linhas + " " + dp + " = ", tipos[linhas][dp]["valores"])
                        