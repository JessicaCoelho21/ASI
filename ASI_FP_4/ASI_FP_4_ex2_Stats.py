# retornar o URL mais visitado
def urlMaisVisitado(urls):
    max = 0;

    for url in urls.keys():
        num_visitas = 0

        for data in urls[url].keys():
            num_visitas += len(urls[url][data])

            if num_visitas > max:
                urlMax = url
                max = num_visitas

    return urlMax, max

# retornar o mês mais visitado
def mesMaisVisitado(urls):
    max = 0

# ordenar por ordem ascendente os urls por mês e ano e por duração do tempo da visita
def timeUrlMaisVisitado(urls):
    geral = {}

    for url in urls.keys():
        order = {}

        for data in urls[url].keys():
            d = str(data).split("/")
            s = str(d[2] + "/" + d[1])

            if s in order.keys():
                for country, duration in urls[url][data]:
                    a_dur = duration.split(":")
                    dur_total = int(a_dur[0]) * 60 * 60 + int(a_dur[1]) * 60 + int(a_dur[2])

                order[s] += dur_total

            else:
                for country, duration in urls[url][data]:
                    a_dur = duration.split(":")
                    dur_total = int(a_dur[0]) * 60 * 60 + int(a_dur[1]) * 60 + int(a_dur[2])

                order[s] = dur_total

        geral[url] = order

    return geral
