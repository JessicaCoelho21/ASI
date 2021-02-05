import re

dados = "912131;2016/02/28 09:20:00"
dias = {'01': 31, '02': 28, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30,
        '12': 31}

pattern = re.compile(r'^(?P<numero>\d{6});'
                     r'(?P<ano>\d{4})\/(?P<mes>\d{2})\/(?P<dia>\d{2})\s(?P<hora>\d{2}):'
                     r'(?P<minutos>\d{2}):(?P<segundos>\d{2})$')
res = pattern.match(dados)

if res:
    if int(res.group('numero')) > 100000 and int(res.group('numero')) < 999999:
        print("Número válido")
        if int(res.group('hora')) <= 9 and int(res.group('minutos')) <= 10 and int(res.group('segundos')) <= 0:
            print("Chegou a Horas")
        else:
            print("Chegou atrasado")

else:
    print("Número inválido!")
