#Semana 2, Exercício 1

idades = [16, 18, 10, 28, 24, 26, 30, 46, 72, 65, 91]

#Idade da pessoa mais nova
idades.sort()
print("Idade da pessoa mais nova:", idades[0])

#Idade da pessoa mais velha
print("Idade da pessoa mais velha:", idades[len(idades) - 1])

#Média das idades
soma = 0
media = 0

for idade in idades:
    soma = soma + idade

media = soma / len(idades)
print("Média das idades:", media)

#Média das idades dos maiores de 18 anos e menores de 65
soma2 = 0
media2 = 0
count = 0

for idade in idades:
    if idade >= 18 and idade <= 65:
        soma2 = soma2 + idade
        count = count + 1

media2 = soma2 / count
print("Média das idades dos maiores de 18 anos e menores de 65:", media2)

