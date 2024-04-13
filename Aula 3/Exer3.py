#Crie um programa em Python que solicite ao usuário a sua idade expressa em anos, meses e dias (variáveis #separadas). Calcule e mostre a idade expressa apenas em dias. Para isso considere 1 ano = 365 dias, 1 mês = #30 dias.
import math
print("    Programa para Converter Idade em Dias ")
print("     Informe as Informações Solicitadas Abaixo:")
ano=int(input("Informe sua idade em ano: "))
meses=int(input("Informe os meses: "))
dias=int(input("Informe os dias: "))
CalcAno=ano*365
CalcMes=meses*30
idadeEmDias=CalcAno+CalcMes+dias
print("Sua idade em dias é:",idadeEmDias)
