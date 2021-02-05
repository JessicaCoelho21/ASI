import re

def Alarm():
    with open("ficheiro.txt") as fp:
        for linhas in fp:
            pattern = re.compile(
                r'^\/(?P<nome>\w*);'
                r'(?P<dia>\d{2})\/(?P<mes>\d{2})\/(?P<ano>\d{4});'
                r'(?P<espacoTotal>\d*);'
                r'(?P<espacoOcupado>\d*)\;'
                r'(?P<warning>\d*);'
                r'(?P<critical>\d*)$')

            res = pattern.match(linhas)
            result = (int(res.group('espacoOcupado')) / int(res.group('espacoTotal'))) * 100

            if result >= 80 and result < 90:
                print("/", res.group('nome'), res.group('dia'), "/", res.group('mes'), "/", res.group('ano'), result, " WARNING")
            elif result >= 90:
                print("/", res.group('nome'), res.group('dia'), "/", res.group('mes'), "/", res.group('ano'), result, " CRITICAL")


def Total(mountpoints):
    valoresMedios = {}
    ocupadoMedios = {}
    valoresMedios1 = {}
    ocupadosMedios1 = {}

    for mtp in mountpoints.keys():
        for data in mountpoints[mtp].keys():
            et = mountpoints[mtp][data]['EspacoTotal']
            if mtp in valoresMedios.keys():
                valoresMedios[mtp].append(float(et))
            else:
                valoresMedios[mtp] = [float(et)]

            ot = mountpoints[mtp][data]['EspacoOcupado']
            if mtp in ocupadoMedios.keys():
                ocupadoMedios[mtp].append(float(ot))
            else:
                ocupadoMedios[mtp] = [float(ot)]

    for k, d in valoresMedios.items():
        valoresMedios1[k] = sum(d) / len(d)

    for k, d in ocupadoMedios.items():
        ocupadosMedios1[k] = sum(d) / len(d)

    return valoresMedios1, ocupadosMedios1
