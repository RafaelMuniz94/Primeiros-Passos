# 6.Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# A = pi*r^2

import math

print("Calcular a área de um círculo")

raio = int(input("Raio do círculo: "))
area = math.pi * math.pow(raio,2)

print("A área do círculo é: ", area)