#Administração de Sistemas Informáticos, 1ª Semana, Exercício 2

data = "8200123;Ana Maria;931221012;12/05/2000"

#Criar um array para separar os dados com ';'
array = data.split(";")
print(array)

#Tamanho do array
print(len(array))

#Adicionar 'SOL' ao array
array.append("SOL")
print(array)

#Conversão da lista final para string
convertion = ",".join(array)
print(convertion)