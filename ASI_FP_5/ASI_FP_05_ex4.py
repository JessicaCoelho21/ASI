# Semana 5, exercício 4

import re

# Verificar se a inicial de todos os nomes se encontra em letra maiúscula
# e as seguintes em letra minúscula

def upperCaseName(name):
    # Início da linha (^) com letra maíuscula seguido de letras minúsculas
    # Seguido do espaço (/s), depois novamente letra maíuscula seguido de letras minúsculas
    # *$ significa que cada caracter, do início ao fim do texto, pode aparecer 0 ou mais vezes
    pattern = re.compile(r'^[A-Z][a-z]+(\s[A-Z][a-z]+)*$')

    if pattern.match(name):
        print("O nome %s obedece ao padrão" % name)

    else:
        print("O nome %s não obedece ao padrão" % name)
