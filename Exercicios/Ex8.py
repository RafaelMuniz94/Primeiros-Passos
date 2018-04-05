#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Cálculadora de salário")

valorHora = int(input("Digite o valor ganho por hora: "))
horasTrabalhadas = int(input("Digite quantas horas foram feitas no mês: "))

total = valorHora * horasTrabalhadas

print("Se salário esse mês será: R$",total)
