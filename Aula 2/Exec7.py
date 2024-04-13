#Escreva um programa em Python que obtenha uma temperatura em graus Celsius, 
#calcule e mostre a respectiva temperatura nas escalas Fahrenheit e Kelvin.
print("    Programa Conversor Celsius para Fahrenheit e Kelvin.")
print("        Informe as Informações Solicitadas Abaixo:")
celsius=float(input("Informe a Temperatura desjada a ser convertida: "))
fahrenheit=(1.8*celsius)+32
kelvin=(celsius+273)
print(f"Fahrenheit: {fahrenheit:.2f}")
print(f"Kelvin: {kelvin:.2f}")
print("Obrigado por Utilizar Meu Programa By: Lucas Freitas")