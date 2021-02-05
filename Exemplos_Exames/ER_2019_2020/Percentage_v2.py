import re

pattern = re.compile(r'^(\/.*;\d{2}\/\d{2}\/\d{4});(\d*);(\d*);(\d*;\d*)$')

with open("ficheiro.txt") as fp:
    for linha in fp:
        linha = linha.strip()
        g = pattern.match(linha)
        if (g):
            perc = format(float(float(g.group(3)) / float(g.group(2))) * 100, '.0f')
            print(pattern.sub(r'\1;\2;' + perc + r';\4', linha))
