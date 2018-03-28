# 9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

print("Conversor de temperatura")

farenheit = int(input("Digite os graus Farenheit: "))

celsius = (5 * (farenheit-32) /9)

print(farenheit,"ºF equivalem à ", celsius, "ºC")