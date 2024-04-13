#Faça uma programa em Python que peça do usuário um valor em graus para um ângulo. Converta-o para radianos e, #usando funções da biblioteca math, imprima o seno, cosseno e tangente deste ângulo.
print("    Programa de Cálculos de Grau ")
print("     Informe as Informações Solicitadas Abaixo:")
import math
grau=float(input("Informe o valor em graus: "))
radiano=180
rc=(3.14)
calcRadiano=(grau*rc)/radiano

seno=math.sin(grau)
cosseno=math.cos(grau)
tangente=math.tan(grau)
print(f"Radiano:{calcRadiano:.5f}")
print(f"Seno:{seno:.5f}")
print(f"Cosseno:{cosseno:.5f}")
print(f"Tangente:{tangente:.5f}")
print("Obrigado por Utilizar Meu Programa By: Lucas Freitas")