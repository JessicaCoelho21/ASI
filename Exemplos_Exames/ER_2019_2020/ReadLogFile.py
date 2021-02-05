def ler():
    monitorizacao = {}

    with open("ficheiro.txt") as fp:
        for linhas in fp:
            linhas = linhas.strip().split(";")

            # Se o primeiro elemento da linha do ficheiro já existir no dicionário
            if linhas[0] in monitorizacao.keys():
                # o dicionário valores tem como chave o segundo elemento do ficheiro,
                # e contém outro dicionário com os restantes dados
                valores = {linhas[1]: {"EspacoTotal": float(linhas[2]),
                                       "EspacoOcupado": float(linhas[3]),
                                       "PercWarning": float(linhas[4]),
                                       "PercCritical": float(linhas[5])}}

                # atualiza o dicionário com o primeiro elemento da linha do ficheiro com o dicionário valores
                monitorizacao[linhas[0]].update(valores)

            # se não existir no deicionário,
            else:
                # atribui diretamente um dicionário com os restantes elementos da linha ao dicionário monitorização
                monitorizacao[linhas[0]] = {linhas[1]: {"EspacoTotal": float(linhas[2]),
                                                        "EspacoOcupado": float(linhas[3]),
                                                        "PercWarning": float(linhas[4]),
                                                        "PercCritical": float(linhas[5])}}

    #print(monitorizacao.items())
    return monitorizacao