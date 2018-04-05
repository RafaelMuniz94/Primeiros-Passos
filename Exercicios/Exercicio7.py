#7.Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
# A = b*h

import math

print("O dobro da área do quadrado")

base = int(input("Digite a base do quadrado:"))
altura = int(input("Digite a altura do quadrado:"))


area = base * altura

print("A área do quadrado é :",area)

area = area * 2

print("O dobro da área do quadrado é: ",area)
