import json
import ASI_FP_4_ex2_Leitura
import ASI_FP_4_ex2_Stats

ficheiro = "dados.txt"

# Função para ler o ficheiro
urls = ASI_FP_4_ex2_Leitura.ler(ficheiro)
print(json.dumps(urls, indent = 4, sort_keys = True))

print("-" * 80)

# retornar o URL mais visitado
url, vezes = ASI_FP_4_ex2_Stats.urlMaisVisitado(urls)
print("O URL %s foi o mais visitado, sendo visitado no total %d vezes." % (url, vezes))

print("-" * 80)

# retornar o mês mais visitado
#month = ASI_FP_4_ex2_Stats.mesMaisVisitado(urls)
#print(json.dumps(month, indent = 4, sort_keys = True))

# ordenar por ordem ascendente os urls por mês e ano e por duração do tempo da visita
order = ASI_FP_4_ex2_Stats.timeUrlMaisVisitado(urls)
print(json.dumps(order, indent = 4, sort_keys = True))
