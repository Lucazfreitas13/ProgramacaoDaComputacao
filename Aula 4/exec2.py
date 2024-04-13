turno = input("Digite o turno de trabalho (N para noturno, D para diurno): ")
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

if turno.upper() == 'N':
    valorHora = 45.00
else:
    valorHora = 37.50

salario = valorHora * horasTrabalhadas

print(f"O valor do salário é: R$ {salario:.2f}")