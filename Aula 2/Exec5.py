#Escreva um programa em Python que leia a cotação do dólar (taxa de conversão),
#leia um valor em dólares e converta e mostre o valor equivalente em Reais
print("    Programa para conversão entre moedas")
print("Informe as Informações Solicitadas Abaixo:")

money=float(input("Informe o valor a ser convertido: "))
dolar=float(input("Contação Dolar: "))
real=float(input("Contação Real: "))
euro=float(input("Contação Euro: "))


conversao_dolar=money/dolar 
conversao_euro=money/euro

print("Você possuí $",conversao_dolar)




print("Obrigado por Utilizar Meu Programa By: Lucas Freitas")
