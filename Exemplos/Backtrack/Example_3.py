import re

str = "8170180; Jessica Beatriz"

pattern = re.compile(r'^(?P<numero>.*);(?P<nome>.*)$')

lista_grupos = pattern.match(str)

if lista_grupos:
    print(lista_grupos.group(2), lista_grupos.group('numero'))