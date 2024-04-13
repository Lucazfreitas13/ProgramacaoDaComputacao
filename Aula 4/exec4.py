salario =float(input("Digite o valor do seu salário: R$ "))
contaAgua=float(input("Digite o valor da conta de água: R$ "))
contaLuz=float(input("Digite o valor da conta de luz: R$ "))
contaTelefone=float(input("Digite o valor da conta de telefone: R$ "))

totalContas = contaAgua + contaLuz + contaTelefone


if salario >= totalContas:
   
    saldoRestante = salario - totalContas
    print("O seu salário é suficiente para pagar as contas!")
    print("Após pagar as contas, você terá R$ {:.2f} restantes.".format(saldoRestante))
else:
    print("Salário insuficiente!")