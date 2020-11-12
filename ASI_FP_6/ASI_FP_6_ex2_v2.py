# Ficha de trabalho da semana 6, exercício 2 (versão 2)
import re

pattern = re.compile(r'^(?P<nome>.*);(?P<idade>.*)$')

with open("dados2.txt") as fp:
    for linha in fp:
        linha = linha.strip()
        matchObj = pattern.match(linha)

        if int(matchObj.group('idade')) < 18:
            print(matchObj.group('nome'), "é menor")

        if int(matchObj.group('idade')) >= 18 and int(matchObj.group('idade')) < 65:
            print(matchObj.group('nome'), "é maior")

        if int(matchObj.group('idade')) > 65:
            print(matchObj.group('nome'), "é sénior")