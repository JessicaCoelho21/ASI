# Ficha de trabalho da semana 6, exercício 2
import re

pattern = re.compile(r'^(.*);(.*)$')

# Converte a idade de string para inteiro
def convert(age):
    ageInt = int(age)
    return ageInt

with open("dados2.txt") as fp:
    for str in fp:
        #str = str.strip()
        list = pattern.match(str)
        # chama a função convert, passando como parâmetro o segundo grupo da lista que obdeceu ao padrão
        age = convert(list.group(2))

        if list:
            print("Match")

            if age < 18:
                print(list.group(1), "é menor de idade, tendo", list.group(2), "anos")

            elif age >= 18 and age <65:
                print(list.group(1), "é maior de idade, tendo", list.group(2), "anos")

            else:
                print(list.group(1), "é sénior, tendo", list.group(2), "anos")

        else:
            print("Doesn't match")
