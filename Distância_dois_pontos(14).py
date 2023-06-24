"""
Programa: Calculadora da distância entre duas coordenadas.
Descrição: Este programa calcula a distância entre dois pontos de um sistema de coordenadas x1 e x2.
Autor: Filipe
Data: 06/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis


#Entrada de dados
x1a = float(input("Qual o valor do ponto x1 da primeira coordenada (x1,x2)? "))
x2a = float(input("Qual o valor do ponto x2 da primeira coordenada (x1,x2)? "))
x1b = float(input("Qual o valor do ponto x1 da primeira coordenada (x1,x2)? "))
x2b = float(input("Qual o valor do ponto x2 da primeira coordenada (x1,x2)? "))

#Processamento de dados

d = ((((x2a-x1a)**2)+((x2b-x1b)**2))**(1/2))

#Saida de dados
print(f"A distância entre os pontos {x1a,x2a} e {x1b,x2b} é {d}.")
