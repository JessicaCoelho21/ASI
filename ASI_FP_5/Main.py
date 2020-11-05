from ASI_FP_05_ex1 import validarCC
from ASI_FP_05_ex2 import people, telephone
from ASI_FP_05_ex3 import countUpperCase
from ASI_FP_05_ex4 import upperCaseName

# Ficha de trabalho 5

# Exercício 1
cc = input("Qual é o numero do cartão de cidadão?: ")
validarCC(cc)

print("-" * 70)

# Exercício 2, alínea a)
people()

# Exercício 2, alínea b)
telephone()

print("-" * 70)

# Exercício 3
text = input("Introduza um texto: ")
countUpperCase(text)

print("-" * 70)

# Exercício 4
name = input("Introduza um texto: ")
upperCaseName(name)

print("-" * 70)