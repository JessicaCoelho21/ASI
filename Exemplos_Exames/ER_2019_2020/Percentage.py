import re

def calculoPercentagem():
    output = {}

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
            res1 = pattern.sub(res.group('nome') + ";" + res.group('dia') + ";" + str(result) + "%;", linhas)

            output = res1

            #print("Percentagem de espaço ocupado: ", res1)

    return output