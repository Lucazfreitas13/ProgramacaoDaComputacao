#Escreva um programa em Python que solicite ao
#usuário o salário atual e mostre o salário acrescido de 5% de comissão.
print("    Programa para Calcular Comissão")
print("Informe as Informações Solicitadas Abaixo:")
salário=float(input("Informe seu salário: "))
comissão=float(salário*0.05)
print(f"Salário: R$ {salário:.2f}")
print(f"Total Comissão: R$ {comissão:.2f}")
print(f"Salário Final: R$ {salário+comissão:.2f}")
print("Obrigado por Utilizar Meu Programa By: Lucas Freitas")
