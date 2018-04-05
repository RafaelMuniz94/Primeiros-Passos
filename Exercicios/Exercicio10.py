# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
# C = (5 * (F-32) / 9). || F = (9 * C + 32)/5


print("Conversor de temperatura")

celsius = int(input("Digite os graus Celsius: "))

farenheit = ((9 * celsius)/5 + 32)

print(celsius,"ºC equivalem à ", farenheit, "ºF") 