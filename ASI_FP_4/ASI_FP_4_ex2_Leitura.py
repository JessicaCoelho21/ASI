# Função para ler o ficheiro
def ler(ficheiro):
    url = {}

    with open(ficheiro) as fp:
        for linha in fp:
            linha = linha.strip().split(";")

            if linha[0] in url.keys():
                visitas = url[linha[0]]
                detalhes_visita = (linha[2], linha[3])

                if linha[1] in visitas.keys():
                    visitas[linha[1]].append(detalhes_visita)

                else:
                    visitas[linha[1]] = [detalhes_visita]

            else:
                visitas = {}
                detalhes_visita = (linha[2], linha[3])
                visitas[linha[1]] = [detalhes_visita]
                url[linha[0]] = visitas

    #ao usar with open(ficheiro) as fp, o ficheiro fecha automaticamente, não sendo preciso usar fp.close()
    return url
