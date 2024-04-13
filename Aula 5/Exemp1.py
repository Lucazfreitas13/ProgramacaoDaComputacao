media=float(input("Digite a Média: "))
frequencia=float(input("Digite o percentual de frequência: "))
if frequencia < 75:
    print("Reprovado por Falta! :(")
elif media < 6:
    print("Reprovado por Nota! :(")
else:
    print("Aprovado! :)")