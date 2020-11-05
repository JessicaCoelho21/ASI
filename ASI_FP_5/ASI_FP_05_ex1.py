import re

# Ficha de trabalho 5, exercício 1

# Expressão regular que valide se o número de Cartão do Cidadão obedece ao padrão (N=número; A=Alfanumérico)

def validarCC(cc):
    # 8 números, espaço, 1 número, espaço, 2 letras, 2 números
    ccRegex = re.search("[0-9]{8}\s[0-9]\s[A-Z]{2}[0-9]", cc)

    if (ccRegex):
        print("O número de cartão de cidadão obdece ao padrão.")
    else:
        print("O número de cartão de cidadão não obdece ao padrão.")
