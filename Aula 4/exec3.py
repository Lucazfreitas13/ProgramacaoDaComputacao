valorCompra = float(input("Digite o valor da compra: R$"))
if valorCompra > 200:
    desconto = 0.2 * valorCompra
    valorFinal = valorCompra - desconto
    print("Como sua compra é superior a R$ 200,00, você ganhou um desconto de 20%")
else:
    valorFinal = valorCompra
print(f"O valor final da compra é: R$ {valorFinal:.2f}")