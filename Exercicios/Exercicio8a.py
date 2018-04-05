#8.1 Faça um Programa que pergunte você ganha por mes e quantas horas foram trabalhadas, e calcule o valor da hora trabalhada


print("Cálculadora valor hora")

horasTrabalhadas = int(input("Digite quantas horas foram feitas no mês: "))
salario = float(input("Digite o valor do seu salário: "))

valorHora = salario/horasTrabalhadas

print("O valor da sua hora é: R$", valorHora)