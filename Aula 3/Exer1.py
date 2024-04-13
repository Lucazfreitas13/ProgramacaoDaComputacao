#Faça um programa em Python que calcule e mostre o valor do volume do tronco de uma pirâmide, para isso o #programa deve solicitar ao usuário os valores da altura do tronco da pirâmide (h), o valor da base menor   
#(Bmenor) e o da base maior (Bmaior) e calcular a seguinte expressão: volume =h/3*(Bmaior**2 + Bmenor**2 + 
#(Bmaior**2 * Bmenor**2)**0.5)
import math
print("    Programa para Calcular o Valor do Volume do Tronco")
print("     Informe as Informações Solicitadas Abaixo:")
h=float(input("Informe o valor de H: "))
bmenor=float(input("Informe o Valor da Base Menor: "))
bmaior=float(input("Informe o Valor da Base Maior: "))
volume=h/3*((math.pow(bmaior,2))+(math.pow(bmenor,2))+((math.pow(bmaior,2))*(math.pow(bmenor,2)))**0.5)
print(f"O Volume do Troco é = {volume:.2f}")
print("Obrigado por Utilizar Meu Programa By: Lucas Freitas")