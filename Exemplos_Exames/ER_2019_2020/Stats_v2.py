from statistics import mean

def Total(res):
    result = {}
    total = {}
    ocupado = {}

    for mount in res.keys():
        for data in res[mount].keys():
            if mount in total.keys():
                total[mount].append(float(res[mount][data]['EspacoTotal']))
            else:
                total[mount] = [float(res[mount][data]['EspacoTotal'])]

            if mount in ocupado.keys():
                ocupado[mount].append(float(res[mount][data]['EspacoOcupado']))
            else:
                ocupado[mount] = [float(res[mount][data]['EspacoOcupado'])]

    for mount in res.keys():
        result[mount] = (mean(total[mount]), mean(ocupado[mount]))

    return result
