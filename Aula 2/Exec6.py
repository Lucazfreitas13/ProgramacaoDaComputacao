#Escreva um programa em Python que leia um valor representando o gasto 
#realizado por um cliente do restaurante ComaBem e visualize o valor total a ser pago, 
#considerando os 10% do garçom.
print("    Programa para Calcular Gorgeta de 10% do Garçon")
print("       Informe as Informações Solicitadas Abaixo:")
totalConsumo=float(input("Digite o Total Consumido pelo Cliente: "))
gorgeta=(totalConsumo*0.10)
print(f"Total Consumo: R$ {totalConsumo:.2f}")
print(f"Total Taxa de Serviço: R$ {gorgeta:.2f}")
print("O Cliente Irá Pagar a Taxa de Serviço?")
opcaoDePagamento=input( "Digite SIM ou NÃO: ")
if opcaoDePagamento == "SIM" or "sim" or "Sim":
    totalAPagar=float(totalConsumo+gorgeta)
else:
    totalAPagar=float(totalConsumo)
print(f"Total a Pagar: R$ {totalAPagar:.2f}")
print("Obrigado por Utilizar Meu Programa By: Lucas Freitas")